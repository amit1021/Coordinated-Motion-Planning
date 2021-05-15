import json
from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
from BFS import bfs , bfs_few_steps

# List of all robot
robot_list = []

# List of robots who reach their destination
robot_in_destination = []

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
row_num = [-1, 0, 0, 1]
col_num = [0, -1, 1, 0]


def init_game():
    # y = 0 that we can choose a board
    y = 0
    # take the board instance
    idb = InstanceDatabase("C:/Users/amite/Desktop/שנה ג/פרויקט/cgshop_2021_instances_01.zip")
    for i in idb:
        print("Instance:", i)
        y = y + 1
        if y == 30:
            break

    # get the board dimensions
    k = json.dumps(i.description)
    l = json.loads(k)
    # The board is n X n
    n = (l['parameters']['shape'][0]) + 10

    # create a board
    board = [[0 for i in range(n)] for j in range(n)]

    i: Instance #just to enable typing
    robot_number = 0
    # create robots
    for r in range(i.number_of_robots):
        # The position of the robot
        start = Point(i.start_of(r)[0] + 5, i.start_of(r)[1] + 5)
        end = Point(i.target_of(r)[0] + 5, i.target_of(r)[1] + 5)
        # Create robot object
        robotObj = Robot(start,end,robot_number)
        # Add robot to robot_list
        robot_list.append(robotObj)
        # Place the robot on the board
        board[robotObj.current_place.x][robotObj.current_place.y] = robotObj.robot_number
        # Update the counter of robots
        robot_number = robot_number + 1

    # Where there is obstacle, put -1 (on board)
    for o in i.obstacles:
        x = o[0] + 5
        y = o[1] + 5
        board[x][y] = -1

    return board


def start_game(board):
    # To check if there is stuck robots.
    stuck = 0
    number_robots = len(robot_list)
    # While there are robots that have not reached their destination
    while len(robot_list) > 0:
        # Go over the robots that did not reach the destination
        for robot in robot_list:
            robot_queue_node = bfs(board, robot.current_place, robot.end_place)
            if robot_queue_node != -1:
                move_robot_all_path(board, robot, robot_queue_node)
            else:
                # Move the robot a few steps the he can
                robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
                move_robot_few_steps(board, robot, robot_queue_node)

            if len(robot_list) == 12 or len(robot_list) == 9 or len(robot_list) == 5:
                stuck = stuck + 1
            else:
                stuck = 0
            number_robots = len(robot_list)
            if stuck > 4:
                robot_stuck(board, robot)
                robot_queue_node = bfs(board, robot.current_place, robot.end_place)
                if robot_queue_node != -1:
                    move_robot_all_path(board, robot, robot_queue_node)
                else:
                    # Move the robot a few steps the he can
                    robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
                    move_robot_few_steps(board, robot, robot_queue_node)

        print("Number of robots that reach their destination:  ", len(robot_in_destination))
        print("Number of robots that are left:  ", len(robot_list))
        print(
            "   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29")
        for i in range(len(board)):
            print( i , board[i])

        if len(robot_list) <= 12:
            print(robot_list)



def move_robot_all_path(board, robot, robot_queue_node):
    # Run on robot's path to the destination
    for p in robot_queue_node.path:
        # Delete the robot from is old place in the board
        board[robot.current_place.x][robot.current_place.y] = 0
        # Update the new point of the robot
        robot.current_place = p
        # Update the board with the new point of the robot
        board[robot.current_place.x][robot.current_place.y] = robot.robot_number
        # When the robot reach is destination
        if Point.equal(robot.current_place, robot.end_place):
            # Remove from robot list
            robot_list.remove(robot)
            # Add to list of the robots who reach their destination
            robot_in_destination.append(robot)

    # Just for checking the function (delete after)
    if not Point.equal(robot.current_place, robot.end_place):
        print("not reach the goal")


def move_robot_few_steps(board,robot, robot_queue_node):
    # Run on robot's path to the destination
    for p in robot_queue_node.path:
        if p == 0:
            # Delete the robot from is old place in the board
            board[robot.current_place.x][robot.current_place.y] = 0
            # Update the new point of the robot
            robot.current_place = p
            # Update the board with the new point of the robot
            board[robot.current_place.x][robot.current_place.y] = robot.robot_number
            # When the robot reach is destination
            if Point.equal(robot.current_place, robot.end_place):
                # Remove from robot list
                robot_list.remove(robot)
                # Add to list of the robots who reach their destination
                robot_in_destination.append(robot)
        else:
            return

    # Just for checking the function (delete after)
    if not Point.equal(robot.current_place, robot.end_place):
        print("not reach the goal")


def robot_stuck(board, robot):
    n = len(board[0])
    x = robot.current_place.x
    y = robot.current_place.y - 1
    z = 5
    if n/2 > robot.current_place.y:
        while y > 0:
            if board[x][y] != -1 and  board[x][y] != 0:
                for robot in robot_in_destination:
                    if robot.robot_number == board[x][y]:
                        move_robot_out_of_board(board,robot,x - z, y)
                        break
            y = y -1
    else:
        while y < n:
            if board[x][y] != -1 and board[x][y] != 0:
                for robot in robot_in_destination:
                    if robot.robot_number == board[x][y]:
                        move_robot_out_of_board(board,robot, x - z, y)
            y = y + 1


def move_robot_out_of_board(board, robot, i, j):
    p = Point(i, j)
    robot_queue_node = bfs(board, robot.current_place, p)
    if robot_queue_node != -1:
        move_robot_all_path(board, robot, robot_queue_node)
    else:
        # Move the robot a few steps the he can
        robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
        move_robot_few_steps(board, robot, robot_queue_node)




def main():
    board = init_game()
    start_game(board)


if __name__ == '__main__':
    main()







# This is a sample Python script.
#
# import json
#
# from Point import Point
# from Robot import Robot
# from cgshop2021_pyutils import Instance
# from cgshop2021_pyutils import InstanceDatabase
#
# from GUI import boardgame1
# from BFS import bfs
#
# # list of all the robots
# robot_list = []
# # List of robots that have reached their destination
# robot_in_dest = []
# # List of robots that have not reached their destination
# move_robot_list = []
#
# # "C:/Users/eli.DESKTOP-58L91HR/Documents/cgshop_2021_instances_01.zip"
# # "C:/Users/amite/Desktop/שנה ג/פרויקט/cgshop_2021_instances_01.zip"
# def init_game():
#     x = 0
#     y = 0
#     idb = InstanceDatabase("C:/Users/amite/Desktop/שנה ג/פרויקט/cgshop_2021_instances_01.zip")
#     for i in idb:
#         print("Instance:", i)
#         y = y + 1
#         if y == 1:
#             break
#
#     # get the board dimensions
#     k = json.dumps(i.description)
#     l = json.loads(k)
#     n = (l['parameters']['shape'][0]) + 10
#     m = (l['parameters']['shape'][1]) + 10
#     print("N: ", n, " M: ", m)
#     # create a board
#     board = [[0 for i in range(n)] for j in range(m)]
#     x = m
#     global boardgame11
#     boardgame11 = boardgame1(x)
#     robnum=1
#
#
#     i: Instance #just to enable typing
#     # create robots
#     for r in range(i.number_of_robots):
#         start = Point(i.start_of(r)[0] + 5, i.start_of(r)[1] + 5)
#         end = Point(i.target_of(r)[0] + 5, i.target_of(r)[1] + 5)
#         r1 = Robot(start,end,robnum)
#         # add robot to robotList
#         robot_list.append(r1)
#         # place the robot on the board
#         board[i.start_of(r)[0]][i.start_of(r)[1]] = r1
#         robnum= robnum+1
#
#     # where there is obstacle, put -1 (on the board)
#     for o in i.obstacles:
#         x = o[0] + 5
#         y = o[1] + 5
#         board[x][y] = -1
#
#
#     for r in robot_list:
#         boardgame11.robot[r.current_place.x][r.current_place.y] = r.num
#         boardgame11.robot1[r.end_place.x][r.end_place.y] = r.num
#     boardgame11.cratetable()
#     return board
#
#
# def isValid(row: int, col: int ,ROW: int, COL: int, board):
#     return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and board[row][col] == 0
#
#
#
#
# def start_game(board):
#     # sum the steps of the robots
#
#     # add all the robots to move_robot_list
#     for r in robot_list:
#         print("robot" , r.num, " ", r.current_place, r.end_place )
#         move_robot_list.append(r)
#
#     # while there are robots that have not yet reached their destination
#     while len(move_robot_list) != 0:
#         # print("number of robot that left: ", len(move_robot_list))
#         # print("number of robot that arrived to destination: ", len(robot_in_dest))
#         # print("steps--------------->", count_steps)
#
#         # running on all the robots on the list
#         for robot_i in move_robot_list:
#             # BFS return queueNode that contains the current place, how many steps left and the path
#             if robot_i.num == 74:
#                 print("   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14   15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30")
#                 for i in range(len(board)):
#                     print( i , board[i])
#             v = bfs(board, robot_i.current_place, robot_i.end_place, robot_i.num)
#             print("number of robot that left: ", len(move_robot_list))
#             print("number of robot that arrived to destination: ", len(robot_in_dest))
#
#             if v != -1:
#                 move_robot1(v.path, robot_i, board)
#
#
# def move_robot(path, robot, board):
#     count_steps = 0
#     for i in range(len(path)):
#         next_step = path[i]
#         # take the current place of the robot
#         prev_x = robot.current_place.x
#         prev_y = robot.current_place.y
#         # delete the robot from the board
#         board[prev_x][prev_y] = 0
#         # boardgame11.robot[prev_x][prev_y] = 0
#         # remove from the lists
#         # move_robot_list.remove(robot)
#         # RobotList2.remove(robot)
#         robot.current_place = next_step
#         count_steps = count_steps + 1
#         board[next_step.x][next_step.y] = robot
#         # boardgame11.robot[next_step.x][next_step.y] = robot.num
#         if Point.equal(robot.current_place, robot.end_place):
#             move_robot_list.remove(robot)
#             robot_in_dest.append(robot)
#     # boardgame11.cratetable()
#     print("steps--------------->", count_steps)
#
# def move_robot1(path, robot, board):
#         prev_x = robot.current_place.x
#         prev_y = robot.current_place.y
#         next_step = path[len(path) - 1]
#         board[prev_x][prev_y] = 0
#         robot.current_place = next_step
#         board[next_step.x][next_step.y] = robot
#         if Point.equal(robot.current_place, robot.end_place):
#             move_robot_list.remove(robot)
#             robot_in_dest.append(robot)
#
#
#     # update robot to the next step
#     # update the robot on the board
#
#
#     # def move_robot(next_step, robot, board):
#     #     # take the current place of the robot
#     #     prev_x = robot.current_place.x
#     #     prev_y = robot.current_place.y
#     #     # delete th robot from the board
#     #     board[prev_x][prev_y] = 0
#     #     boardgame11.robot[prev_x][prev_y] = 0
#     #     # remove from the lists
#     #     # move_robot_list.remove(robot)
#     #     # RobotList2.remove(robot)
#     #
#     #     # update robot to the next step
#     #     robot.current_place = next_step
#     #     # update the robot on the board
#     #     board[next_step.x][next_step.y] = robot
#     #     boardgame11.robot[next_step.x][next_step.y] = robot.num
#     #     if Point.equal(robot.current_place, robot.end_place):
#     #         move_robot_list.remove(robot)
#     #         robot_in_dest.append(robot)
#     #     boardgame11.cratetable()
#
#
# # ---------------------- Example ---------------------------
# def example():
#
#     x = 10
#     robotMatrix2 = [[0 for i in range(x)] for j in range(x)]
#     global boardgame11
#     boardgame11 = boardgame1(x)
#     r1 = Robot(Point(0, 0), Point(6, 7), 1)
#     r2 = Robot(Point(1, 1), Point(8, 6), 2)
#     r3 = Robot(Point(8, 0), Point(0, 9), 3)
#
#     robot_list.append(r1)
#     robot_list.append(r2)
#     robot_list.append(r3)
#
#     for r in robot_list:
#         boardgame11.robot[r.current_place.x][r.current_place.y] = r.num
#         boardgame11.robot1[r.end_place.x][r.end_place.y] = r.num
#
#     robotMatrix2[0][0] = r1
#     robotMatrix2[1][1] = r2
#     robotMatrix2[8][0] = r3
#     boardgame11.cratetable()
#
#     return robotMatrix2
#
# # ---------------------------------------------------------
#
#
# def main():
#     board = init_game()
#     #board = init_game()
#     start_game(board)
# if __name__ == '__main__':
#     main()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def move_robot_in_destination(robot, board, robot_destination):
# #     # These arrays are used to get row and column
# #     # numbers of 4 neighbours of a given cell
# #     rowNum = [-1, 0, 0, 1]
# #     colNum = [0, -1, 1, 0]
# #     for i in range(4):
# #         row = robot.current_place.x + rowNum[i]
# #         col = robot.current_place.y + colNum[i]
# #         if isValid(row, col, len(board), len(board), board):
# #             board[robot.current_place.x][robot.current_place.y] = 0
# #             robot.current_place = Point(row,col)
# #             board[row][col] = robot
# #             if robot_destination == True:
# #                 robot_in_dest.remove(robot)
# #                 move_robot_list.append(robot)
# #         return
#
#
# # flag - to check if the next step is the destination of some robot
# # flag = False
# # if board[next_step.x][next_step.y] != 0:
# #
# #     for r_dest in robot_in_dest:
# #         if next_step == r_dest.end_place:
# #             count_steps = count_steps + 1
# #             move_robot_in_destination(r_dest, board, True)
# #             robot_i.stuck = 0
# #             flag = True
# #
# #     if flag is False and robot_i.stuck == 2:
# #         r_dest = board[next_step.x][next_step.y]
# #         count_steps = count_steps + 1
# #         move_robot_in_destination(r_dest, board, False)
# #         robot_i.stuck = 0
# #
# #     elif flag is False and robot_i.stuck < 2:
# #         robot_i.stuck = robot_i.stuck + 1
# #
# # if board[next_step.x][next_step.y] == 0:
# #     move_robot(next_step, robot_i, board)
# #     count_steps = count_steps + 1
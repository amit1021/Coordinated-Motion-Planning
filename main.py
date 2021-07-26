
from GUI import boardgame1
from Init_fram import frames, get_robot_out
from MoveRobots import move_robot_all_path, move_robot_few_steps, moveRobotStuck
from Move_Robot import move_robot, move_robot_to_dest
from Point import Point
import time
from BFS import bfs, bfs_few_steps
from initTheGame import init_game

from params import getRobotListDestSize, getRobotToListNot_destSize, getRobotToListNot_dest, robot_list, FindRobotByNumber


def start_game(board):
    # To check if there is stuck robots.
    stuck = 0
    number_robots = getRobotToListNot_destSize()
    number_of_steps = 0


    # GUI
    boardgame2 = boardgame1(len(board))
    for r in robot_list:
        boardgame2.robot[r.current_place.x][r.current_place.y] = r.robot_number
        boardgame2.robot1[r.end_place.x][r.end_place.y] = r.robot_number
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    boardgame2.robot1[i][j] = -1
    boardgame1.cratetable(boardgame2)


    # While there are robots that have not reached their destination
    while getRobotToListNot_destSize() > 0:
       # Go over the robots that did not reach the destination
        for robot in getRobotToListNot_dest():
            robot_queue_node = bfs(board, robot.current_place, robot.end_place)
            if robot_queue_node != -1:
                number_of_steps = move_robot_all_path(board, robot, robot_queue_node, boardgame2, number_of_steps)
            else:
                # Move the robot a few steps the he can
                robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
                number_of_steps = move_robot_few_steps(board, robot, robot_queue_node, boardgame2, number_of_steps)
            print("Number of steps: ", number_of_steps)

        print("Number of robots that reach their destination:  ", getRobotListDestSize())
        print("Number of robots that are left:  ", len(getRobotToListNot_dest()))

        if getRobotToListNot_destSize() == number_robots:
            stuck = stuck + 1
        else:
            stuck = 0

        if getRobotToListNot_destSize() != number_robots:
            number_robots = getRobotToListNot_destSize()

        if stuck >= 4:
            counter = 1
            print(getRobotToListNot_dest())
            if counter == 1:
                print(" debug")
            for robot in getRobotToListNot_dest():
                if getRobotToListNot_destSize() == 1:
                    print("one left")
                number_of_steps = moveRobotStuck(board, robot, boardgame2, number_of_steps)
                print("Number of steps: ", number_of_steps)


            print(
                "   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29")
            for i in range(len(board)):
                print(i, board[i])


def start_game2(board):
    n = len(board)
    number_of_steps = 0
    robot_final_place = [[0 for i in range(n)] for j in range(n)]
    for r in robot_list:
        robot_final_place[r.end_place.x][r.end_place.y] = r.robot_number

   # GUI
    boardgame2 = boardgame1(len(board))
    for r in robot_list:
        boardgame2.robot[r.current_place.x][r.current_place.y] = r.robot_number
        boardgame2.robot1[r.end_place.x][r.end_place.y] = r.robot_number
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    boardgame2.robot1[i][j] = -1
    boardgame1.cratetable(boardgame2)

    number_of_robot = len(robot_list)
    blank_spcae = 0
    count = number_of_robot
    q = 0
    while count > 0:
        count -= (len(board) - q) * 4
        q += 2
        blank_spcae += 1
    print("number of blank: " ,blank_spcae)

    num = frames(board, boardgame2,blank_spcae)
    number_of_steps +=num

    print("number_of_steps: ",number_of_steps)

    a = int(n/2)
    b = int(n/2)
    r = c = len(robot_final_place)
    low_row = 0 if (0 > a) else a
    low_column = 0 if (0 > b) else b - 1
    high_row = r - 1 if ((a + 1) >= r) else a + 1
    high_column = c - 1 if ((b + 1) >= c) else b + 1

    while ((low_row > 0 - r and low_column > 0 - c)):
        i = low_column + 1
        while (i <= high_column and
               i < c and low_row >= 0):
            if robot_final_place[low_row][i] >= 1:
                robot = FindRobotByNumber(robot_final_place[low_row][i])
                if robot != -1:
                    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        num = move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
                        number_of_steps += num
                    else:
                        get_robot_out(board, robot, boardgame2, blank_spcae)
                else:
                    print("robot equal -1")
            print("number_of_steps: ", number_of_steps)

            i += 1
        low_row -= 1

        i = low_row + 2
        while (i <= high_row and
               i < r and high_column < c):
            if robot_final_place[i][high_column] >= 1:
                robot = FindRobotByNumber(robot_final_place[i][high_column])
                if robot != -1:
                    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        num = move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
                        number_of_steps += num
                    else:
                        get_robot_out(board, robot, boardgame2, blank_spcae)
                else:
                    print("robot equal -1")
            print("number_of_steps: ", number_of_steps)

            i += 1
        high_column += 1

        i = high_column - 2
        while (i >= low_column and
               i >= 0 and high_row < r):
            if robot_final_place[high_row][i] >= 1:
                robot = FindRobotByNumber(robot_final_place[high_row][i])
                if robot != -1:
                    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                       num = move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
                       number_of_steps += num
                    else:
                        get_robot_out(board, robot, boardgame2, blank_spcae)
                else:
                    print("robot equal -1")
            print("number_of_steps: ", number_of_steps)

            i -= 1
        high_row += 1

        i = high_row - 2
        while (i > low_row and
               i >= 0 and low_column >= 0):
            if robot_final_place[i][low_column] >= 1:
                robot = FindRobotByNumber(robot_final_place[i][low_column])
                if robot != -1:
                    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        num = move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
                        number_of_steps += num
                    else:
                        get_robot_out(board, robot, boardgame2, blank_spcae)
                else:
                    print("robot equal -1")
            print("number_of_steps: ", number_of_steps)
            i -= 1
        low_column -= 1

    for r in robot_list:
        if not Point.equal(r.current_place, r.end_place):
            print("r.current_place: ", r.current_place)
            print("r.end_place: ", r.end_place)
            print("robot number ", r.robot_number)
            print("not good!!")

    print("number_of_steps: ",number_of_steps)

    time.sleep(10)


def add_steps(n, number_of_steps):
    number_of_steps += n
    return number_of_steps

def main():
    board = init_game()
    # start_game(board)
    start_game2(board)


if __name__ == '__main__':
    main()

import json
from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase

from params import addRobotToList, addRobotToListNot_dest


def init_game():
    # y = 0 that we can choose a board
    y = 0
    # take the board instance
    idb = InstanceDatabase("C:/Users/amit.elbaz/Desktop/Amit/cgshop_2021_instances_01.zip")
    for i in idb:
        print("Instance:", i)
        print(y + 1)
        y = y + 1
        if y == 23:
            break

    # get the board dimensions
    k = json.dumps(i.description)
    l = json.loads(k)
    # The board is n X n
    n = (l['parameters']['shape'][0])
    length_board = n

    i: Instance #just to enable typing

    q = blank_space(i.number_of_robots, n)
    n = (l['parameters']['shape'][0]) + (2 * q)

    # create board with the final place of the robots
    robot_final_place = [[0 for i in range(n)] for j in range(n)]

    # create a board
    board = [[0 for i in range(n)] for j in range(n)]

    print("len borad : ", len(board))

    robot_number = 0
    # create robots
    for r in range(i.number_of_robots):

        # The position of the robot
        # start = Point(i.start_of(r)[0] + q , i.start_of(r)[1] + q)
        # end = Point(i.target_of(r)[0] + q, i.target_of(r)[1] + q)

        start = Point(i.start_of(r)[0] + q, i.start_of(r)[1] + q)
        end = Point(i.target_of(r)[0] + q, i.target_of(r)[1] + q)

        # Create robot object
        robotObj = Robot(start,end,robot_number)

        # Add robot to robot_list
        addRobotToList(robotObj)
        addRobotToListNot_dest(robotObj)

        # Place the robot on the board
        board[robotObj.current_place.x][robotObj.current_place.y] = robotObj.robot_number
        # Place the robot on the robot_final_place
        robot_final_place[end.x][end.y] = robotObj.robot_number

        # Update the counter of robots
        robot_number = robot_number + 1

    # Where there is obstacle, put -1 (on board)
    for o in i.obstacles:
        # x = o[0] + 3 + blank_spcae
        # y = o[1] + 3 + blank_spcae
        x = o[0] + q
        y = o[1] + q
        board[x][y] = -1
        robot_final_place[x][y] = -1

    return board, length_board, robot_final_place


def blank_space(number_of_robots, n):
    # Finds how many lines to add to the board
    blank_spcae = 0
    count = number_of_robots
    q = 0
    while count > 0:
        count -= (n - q) * 4
        q += 2
        blank_spcae += 1
    print("number of blank: ", blank_spcae)

    # board length with expansion
    x = blank_spcae + 2
    # if n > 99 and number_of_robots >= 2500:
    #     x = blank_spcae + 4
    return x

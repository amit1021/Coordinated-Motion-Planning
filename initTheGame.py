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
        if y == 102:
            break

    # get the board dimensions
    k = json.dumps(i.description)
    l = json.loads(k)
    # The board is n X n
    n = (l['parameters']['shape'][0])

    i: Instance #just to enable typing

    # Finds how many lines to add to the board
    blank_spcae = 0
    count = i.number_of_robots
    q = 0
    while count > 0:
        count -= (n - q) * 4
        q += 2
        blank_spcae += 1
    print("number of blank: ", blank_spcae)

    # board length with expansion
    x = 2 * (3 + blank_spcae)
    n = (l['parameters']['shape'][0]) + x
    #
    q = 3 + blank_spcae
    # create a board
    board = [[0 for i in range(n)] for j in range(n)]

    print("len borad : ", len(board))

    robot_number = 0
    # create robots
    for r in range(i.number_of_robots):

        # The position of the robot
        # start = Point(i.start_of(r)[0] + q , i.start_of(r)[1] + q)
        # end = Point(i.target_of(r)[0] + q, i.target_of(r)[1] + q)

        start = Point(i.start_of(r)[0] + 3 + blank_spcae, i.start_of(r)[1] + 3 + blank_spcae)
        end = Point(i.target_of(r)[0] + 3 + blank_spcae, i.target_of(r)[1] + 3 + blank_spcae)

        # Create robot object
        robotObj = Robot(start,end,robot_number)

        # Add robot to robot_list
        addRobotToList(robotObj)
        addRobotToListNot_dest(robotObj)

        # Place the robot on the board
        board[robotObj.current_place.x][robotObj.current_place.y] = robotObj.robot_number
        # Update the counter of robots
        robot_number = robot_number + 1

    # Where there is obstacle, put -1 (on board)
    for o in i.obstacles:
        # x = o[0] + 3 + blank_spcae
        # y = o[1] + 3 + blank_spcae
        x = o[0] + q
        y = o[1] + q
        board[x][y] = -1

    return board

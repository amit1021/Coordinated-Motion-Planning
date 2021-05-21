import json
from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase


# List of all robot

# robot_list = []
from params import addRobotToList, addRobotToListNot_dest


def init_game():
    # y = 0 that we can choose a board
    y = 0
    # take the board instance
    idb = InstanceDatabase("C:/Users/amite/Desktop/שנה ג/פרויקט/cgshop_2021_instances_01.zip")
    for i in idb:
        print("Instance:", i)
        y = y + 1
        if y == 7:
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
        addRobotToList(robotObj)
        addRobotToListNot_dest(robotObj)
                                # robot_list.append(robotObj)
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
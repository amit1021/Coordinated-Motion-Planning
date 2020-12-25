# This is a sample Python script.

import json
from cgshop2021_pyutils import Solution, SolutionStep, SolutionZipWriter, Direction
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
import numpy as np

from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase

from queueNode import queueNode
from shortestPath import BFS

# list of all the robots
robot_list = []
RobotList2 = []

def init_game():
    x=0
    idb = InstanceDatabase("C:/Users/amite/Desktop/שנה ג/פרויקט/cgshop_2021_instances_01.zip")
    for i in idb:
        print("Instance:", i)
        x = x + 1
        if x == 2:
            break

    # get the board dimensions
    k = json.dumps(i.description)
    l = json.loads(k)
    n = (l['parameters']['shape'][0])
    m = (l['parameters']['shape'][1])
    # create a board
    board = [[0 for i in range(n)] for j in range(m)]


    i: Instance #just to enable typing
    # create robots
    for r in range(i.number_of_robots):
        start = Point(i.start_of(r)[0], i.start_of(r)[1])
        end = Point(i.target_of(r)[0], i.target_of(r)[1])
        r1 = Robot(start,end)
        # add robot to robotList
        robot_list.append(r1)
        # place the robot on the board
        board[i.start_of(r)[0]][i.start_of(r)[1]] = r1

    # where there is obstacle, put -1 (on the board)
    for o in i.obstacles:
        x = o[0]
        y = o[1]
        board[x][y] = -1
    return board



# def start_game(board):
#
#     for i in robot_list:
#         a = BFS(board, i.current_place, i.end_place)
#
#         ==========
#         moveRobot()
#
#         if(r.currPlace == endPalce)
#
#         print(a)
#         # for p in a.path:
#         #     print("X=  " + p[0] + "  Y = " + p[1])





# ---------------------- Example ---------------------------

def move_robot(next_step, robot, board, move_robot_list):
    # take the current place of the robot
    prev_x = robot.current_place.x
    prev_y = robot.current_place.y
    # delete th robot from the board
    board[prev_x][prev_y] = 0
    #remove from the lists
    move_robot_list.remove(robot)
    RobotList2.remove(robot)
    # update robot to the next step
    robot.current_place = next_step
    # update the robot on the board
    board[next_step.x][next_step.y] = robot
    if (robot.current_place.x == robot.end_place.x
            and robot.current_place.y == robot.end_place.y):
        robot_list.append(robot)
        return
    else:
        #add to the lists
        move_robot_list.append(robot)
        robot_list.append(robot)

def example():
    r1 = Robot(Point(0,0), Point(0,3))
    r2 = Robot (Point(2,2), Point(3,3))
    r3 = Robot(Point(1,1), Point(3,0))


    RobotList2.append(r1)
    RobotList2.append(r2)
    RobotList2.append(r3)
    robotMatrix2 = [[0 for i in range(4)] for j in range(4)]
    robotMatrix2[0][0] = r1
    robotMatrix2[2][2] = r2
    robotMatrix2[1][1] = r3
    move_robot_list = []

    for r in RobotList2:
        move_robot_list.append(r)

    while len(move_robot_list) != 0:
        for robot_i in RobotList2:
            # if (robot_i.current_place.x == robot_i.end_place.x
            #         and robot_i.current_place.y == robot_i.end_place.y):
            #     print("in the if")
                # move_robot_list.remove(robot_i)
            v = BFS(robotMatrix2, robot_i.current_place, robot_i.end_place)
            next_step = v.path[0]
            move_robot(next_step, robot_i, robotMatrix2, move_robot_list)

    print(robotMatrix2)


# ---------------------------------------------------------


def main():
    example()
    # board = init()


if __name__ == '__main__':
    main()
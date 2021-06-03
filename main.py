import json

# import MoveRobots import move_robot_all_path, move_robot_few_steps
import pygame

from GUI import boardgame1
from MoveRobots import move_robot_all_path, move_robot_few_steps, moveRobotStuck
from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
from BFS import bfs, bfs_few_steps
from initTheGame import init_game
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
from params import getRobotListDestSize, getRobotToListNot_destSize, getRobotToListNot_dest, robot_list, addRobotToList, \
    addRobotToListNot_dest


def start_game(board):
    # To check if there is stuck robots.
    stuck = 0
    number_robots = getRobotToListNot_destSize()
    # the next lines for the gui
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
                move_robot_all_path(board, robot, robot_queue_node, boardgame2)
            else:
                # Move the robot a few steps the he can
                robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
                move_robot_few_steps(board, robot, robot_queue_node, boardgame2)

        print("Number of robots that reach their destination:  ", getRobotListDestSize())
        print("Number of robots that are left:  ", len(getRobotToListNot_dest()))

        if getRobotToListNot_destSize() == number_robots:
            stuck = stuck + 1
        else:
            stuck = 0

        if getRobotToListNot_destSize() != number_robots:
            number_robots = getRobotToListNot_destSize()

        if stuck >= 4:
            print(getRobotToListNot_dest())
            for robot in getRobotToListNot_dest():
                if getRobotToListNot_destSize() == 1:
                    print("one left")
                moveRobotStuck(board, robot, boardgame2)
            # print(
            #     "   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29")
            # for i in range(len(board)):
            #     print(i, board[i])


def main():

        board = init_game()
        start_game(board)

if __name__ == '__main__':
    main()






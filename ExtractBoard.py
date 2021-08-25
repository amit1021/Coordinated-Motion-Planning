import json
import IncreaseBoard

from typing import List, Any

from Gui import Gui
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
from Point import Point
from IncreaseBoard import row_space
from RobotDetails import robot_list


class ExtractBoard:
    def __init__(self, board_number):
        self.board_number = board_number
        self.board = [[]]
        self.board_final_state = [[]]
        self.number_of_robots = None
        self.n_original = None
        self.n = None
        self.row_space = None
        self.i = None
        self.board_ui = None

    def extract_board(self):
        # take the board instance
        curr_board_number = 0
        idb = InstanceDatabase("C:/Users/amit.elbaz/Desktop/Amit/cgshop_2021_instances_01.zip")
        for i in idb:
            curr_board_number += 1
            if self.board_number == curr_board_number:
                break

        # get the board dimensions
        board_description = json.dumps(i.description)
        board_params = json.loads(board_description)
        # The board is n X n
        self.n_original = (board_params['parameters']['shape'][0])
        self.number_of_robots = i.number_of_robots
        # increasing board by the algorithm
        self.row_space = row_space(self.number_of_robots, self.n_original)
        print(self.row_space)
        self.n = (board_params['parameters']['shape'][0]) + (2 * self.row_space)

        i: Instance  # just to enable typing
        self.i = i
        # create a board
        board = [[0 for i in range(self.n)] for j in range(self.n)]
        self.board = board
        # create board with the final place of the robots
        self.board_final_state = [[0 for i in range(self.n)] for j in range(self.n)]
        self.board_ui = Gui(self.n)
        self.fill_board()

    def fill_board(self):
        i = self.i
        robot_number = 0
        for r in range(i.number_of_robots):
            # The position of the robot
            start = Point(i.start_of(r)[0] + self.row_space, i.start_of(r)[1] + self.row_space)
            end = Point(i.target_of(r)[0] + self.row_space, i.target_of(r)[1] + self.row_space)
            # Create robot object
            robot = Robot(start, end, robot_number)
            # add robot to robotList
            robot_list.append(robot)
            # place the robot on the board
            self.board[start.x][start.y] = robot.robot_number
            self.board_final_state[end.x][end.y] = robot.robot_number
            self.board_ui.src[start.x][start.y] = robot.robot_number
            self.board_ui.dest[end.x][end.y] = robot.robot_number
            robot_number += 1

        # Where there is obstacle, put -1 (on board)
        for o in i.obstacles:
            x = o[0] + self.row_space
            y = o[1] + self.row_space
            self.board[x][y] = -1
            self.board_final_state[x][y] = -1
            self.board_ui.dest[x][y] = - 1

import IncreaseBoard
from InitFrames import init_frames
from InsertInSpiral import insert_in_spiral
from MoveRobot import move_robot_after_finish


def start_game(eb):
    number_of_steps = 0
    eb.row_space = IncreaseBoard.row_space_final(eb.number_of_robots, eb.n, eb.row_space)
    number_of_steps += init_frames(eb)
    number_of_steps += insert_in_spiral(eb)
    number_of_steps += move_robot_after_finish(eb)
    return number_of_steps

from BFS import bfs, bfs_few_steps
from Point import Point

from params import addRobotToDest, removeRobotToListNot_dest, FindRobotByNumber, addRobotToListNot_dest, \
    removeRobotToDest


def move_robot(board, robot, robot_queue_node ,boardgame1):
    number_of_steps = 0
    # Run on robot's path to the destination
    for p in robot_queue_node.path:
        # Delete the robot from is old place in the board
        board[robot.current_place.x][robot.current_place.y] = 0
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = 0
        # Update the new point of the robot
        robot.current_place = p
        # Update the board with the new point of the robot
        board[robot.current_place.x][robot.current_place.y] = robot.robot_number

        boardgame1.robot[robot.current_place.x][robot.current_place.y] = robot.robot_number
        number_of_steps += 1
        # Add step
        # number_of_steps = number_of_steps + 1

    boardgame1.cratetable()
    return number_of_steps


def move_robot_to_dest(board, robot, robot_queue_node, boardgame1):
    number_of_steps = 0
    # Run on robot's path to the destination
    for p in robot_queue_node.path:
        # Delete the robot from is old place in the board
        board[robot.current_place.x][robot.current_place.y] = 0
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = 0
        # Update the new point of the robot
        robot.current_place = p
        # Update the board with the new point of the robot
        board[robot.current_place.x][robot.current_place.y] = robot.robot_number

        boardgame1.robot[robot.current_place.x][robot.current_place.y] = robot.robot_number
        number_of_steps += 1
        # if Point.equal(robot.current_place, robot.end_place):
        #     # Remove from robot list
        #     removeRobotToListNot_dest(robot)
        #     # Add to list of the robots who reach their destination
        #     addRobotToDest(robot)

    boardgame1.cratetable()
    return number_of_steps


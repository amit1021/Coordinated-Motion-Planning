from BFS import bfs, bfs_few_steps
from Point import Point
from main import robot_list, robot_in_destination


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


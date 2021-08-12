# List of all robot
robot_list = []


def find_robot_by_number(num):
    for robot in robot_list:
        if robot.robot_number == num:
            return robot
    return -1


# List of all robot
robot_list = []

# List of robots who reach their destination
robot_in_destination = []

# List of robots who not reach their destination
robot_list_not_dest = []


def addRobotToList(robot):
    robot_list.append(robot)
    return


def addRobotToListNot_dest(robot):
    robot_list_not_dest.append(robot)
    return


def removeRobotToListNot_dest(robot):
    robot_list_not_dest.remove(robot)
    return


def removeRobotFromList(robot):
    robot_list.remove(robot)
    return


def addRobotToDest(robot):
    robot_in_destination.append(robot)
    return


def removeRobotToDest(robot):
    robot_in_destination.remove(robot)
    return


def getRobotListSize():
    return len(robot_list)


def getRobotList():
    return robot_list


def getRobotListDest():
    return robot_in_destination


def getRobotListDestSize():
    return len(robot_in_destination)


def getRobotToListNot_destSize():
    return len(robot_list_not_dest)


def getRobotToListNot_dest():
    return robot_list_not_dest


def FindRobotByNumber(num):
    for robot in robot_list:
        if robot.robot_number == num:
            return robot
    return -1


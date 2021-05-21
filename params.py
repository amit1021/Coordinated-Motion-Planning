
# List of all robot
robot_list = []

# List of robots who reach their destination
robot_in_destination = []

def addRobotToList(robot):
    robot_list.append(robot)
    return


def removeRobotFromList(robot):
    robot_list.remove(robot)
    return


def addRobotToDest(robot):
    robot_in_destination.append(robot)
    return


def getRobotListSize():
    return len(robot_list)


def getRobotList():
    return robot_list


def getRobotListDest():
    return robot_in_destination


def getRobotListDestSize():
    return len(robot_in_destination)
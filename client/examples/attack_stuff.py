
from botchallenge import *
import time

USERNAME = "rafi0t" # Put your minecraft username here
SERVER = "10.2.113.180" # Put the address of the minecraft server here

robot = Robot(USERNAME, SERVER)

while True:
    me = robot.get_location()
    owner = robot.get_owner_location()

    print(me.distance(owner))
    if me.distance(owner) > 4:
        d = robot.find_path(owner)
        robot.turn(d)
        robot.move(d)
    else:
        #robot.attack(robot.get_owner_location())
        robot.get_entities()
        time.sleep(2)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from botchallenge import Robot
from botchallenge import Dir
from botchallenge import Location


USERNAME = "rafi0t"  # Put your minecraft username here
SERVER = "localhost"  # Put the address of the minecraft server here
robot = Robot(USERNAME, SERVER)

robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=64)


# 1. Move up, down, east, west, north, south
#    Between each move, print the location of your robot

robot.move(Dir.UP)
robot.get_location()
# Location(x_coord=-104, y_coord=85, z_coord=64)
robot.move(Dir.DOWN)
robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=64)
robot.move(Dir.EAST)
robot.get_location()
# Location(x_coord=-103, y_coord=84, z_coord=64)
robot.move(Dir.WEST)
robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=64)
robot.move(Dir.NORTH)
robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=63)
robot.move(Dir.SOUTH)
robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=64)


# 2. Choose the coordinates you want your robot to go to
#    Compute the values of x, y and z of your vector

location_origin = robot.get_location()
# Location(x_coord=-104, y_coord=84, z_coord=64)
location_destination = Location(x_coord=-104, y_coord=84, z_coord=80)

location_origin.x_coord
# -104
location_origin.y_coord
# 84
location_origin.z_coord
# 64
location_destination.x_coord
# -104
location_destination.y_coord
# 84
location_destination.z_coord
# 80

# location_origin.x_coord + x = location_destination.x_coord
# -104 + x = -104
# x = 0

# location_origin.y_coord + y = location_destination.y_coord
# 84 + y = 84
# y = 0

# location_origin.z_coord + z = location_destination.z_coord => x = 0
# 64 + z = 80
# z = 16

# z moves up when the robot goes south

# 3. move your robot to the right place with up, down...
#    Print the location to see if you go in the right direction

robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)
robot.move(Dir.SOUTH)


# 4. Go back to the original point in a loop

for i in range(16):
    robot.move(Dir.NORTH)

# 5. How to compute the values of x, y an z more easily?

path = location_destination - location_origin
# Location(x_coord=0, y_coord=0, z_coord=16)

# Bonus: do the same but change more than one coordinate

# 6. Think about a way to go to the right place by using what we learned before
# Hint: the function find_path() will help

while robot.get_location() != location_destination:
    path = robot.find_path(location_destination)
    robot.move(path)
    print(robot.get_location())

# 7. Make it a function

def goto(robot, destination):
    while robot.get_location() != destination:
        robot.move(robot.find_path(destination))

# Note: Your robot may still get stuck

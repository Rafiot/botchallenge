#!/usr/bin/env python
# -*- coding: utf-8 -*-

from botchallenge import Robot


USERNAME = "rafi0t"  # Put your minecraft username here
SERVER = "localhost"  # Put the address of the minecraft server here
robot = Robot(USERNAME, SERVER)

robot.get_location()

# 1. Move up, down, east, west, forward, backward
#    Between each move, print the location of your robot

# 2. Choose the coordinates you want your robot to go to
#    Compute the values of x, y and z of your vector

# 3. move your robot to the right place with up, down...
#    Print the location to see if you go in the right direction

# 4. Go back to the original point in a loop

# 5. How to compute the values of x, y an z more easily?

# Bonus: do the same but change more than one coordinate

# 6. Think about a way to go to the right place by using what we learned before
# Hint: the function find_path() will help

# 7. Make it a function


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from botchallenge import Robot
from botchallenge import BlockType
from botchallenge import Dir
# from botchallenge import Location

USERNAME = "rafi0t"  # Put your minecraft username here
SERVER = "localhost"  # Put the address of the minecraft server here
robot = Robot(USERNAME, SERVER)

# 1. What do you want to mine?

elements = [BlockType.DIAMOND, BlockType.GOLD_ORE, BlockType.IRON_ORE,
            BlockType.COAL_ORE]


# 2. Look for the blocks, and stop as soon as we have something

locations = []

for e in elements:
    locs = robot.find_type_nearby(e)
    if len(locs) > 0:
        locations = locs
        break

print(locations)
# You have a hit: [Location(x_coord=-108, y_coord=70, z_coord=201, ...]
# or
# You don't: []

# Do you have something? If not, dig down:

# Move to the ground:
while robot.move(Dir.DOWN):
    continue

# Dig 10 blocks down

for i in range(10):
    robot.mine(Dir.DOWN)
    robot.move(Dir.DOWN)

# Look for elements with the code you wrote earlier
# If you still don't find anything, dig in some other directions until you have a hit


# 3. Go mine!
# Hint: You may have other blocks between you and the block you want.
# In that case, just mine your way through.


for loc in locations:
    path = loc - robot.get_location()
    print('Robot:', robot.get_location())
    print('Dest:', loc)
    print('path:', path)
    x, y, z = path
    while x != 0:
        if x > 0:
            if robot.is_block_solid(Dir.EAST):
                robot.mine(Dir.EAST)
            robot.move(Dir.EAST)
            x -= 1
        else:
            if robot.is_block_solid(Dir.WEST):
                robot.mine(Dir.WEST)
            robot.move(Dir.WEST)
            x += 1
    print(robot.get_location())
    while y != 0:
        if y > 0:
            if robot.is_block_solid(Dir.UP):
                robot.mine(Dir.UP)
            robot.move(Dir.UP)
            y -= 1
        else:
            if robot.is_block_solid(Dir.DOWN):
                robot.mine(Dir.DOWN)
            robot.move(Dir.DOWN)
            y += 1
    print(robot.get_location())
    while z != 0:
        if z > 0:
            if robot.is_block_solid(Dir.SOUTH):
                robot.mine(Dir.SOUTH)
            robot.move(Dir.SOUTH)
            z -= 1
        else:
            if robot.is_block_solid(Dir.NORTH):
                robot.mine(Dir.NORTH)
            robot.move(Dir.NORTH)
            z += 1
    print(robot.get_location())

robot.get_inventory()

# Refactoring

def force_move(direction):
    if robot.is_block_solid(direction):
        robot.mine(direction)
    robot.move(direction)


for loc in locations:
    path = loc - robot.get_location()
    x, y, z = path
    while x != 0:
        if x > 0:
            force_move(Dir.EAST)
            x -= 1
        else:
            force_move(Dir.WEST)
            x += 1
    while y != 0:
        if y > 0:
            force_move(Dir.UP)
            y -= 1
        else:
            force_move(Dir.DOWN)
            y += 1
    while z != 0:
        if z > 0:
            force_move(Dir.SOUTH)
            z -= 1
        else:
            force_move(Dir.NORTH)
            z += 1

# More refactoring
for loc in locations:
    while True:
        curr_location = robot.get_location()
        direction = curr_location.direction(loc)
        if direction is None:
            break
        force_move(direction)

# And even shorter
for loc in locations:
    while True:
        direction = robot.get_location().direction(loc)
        if direction is None:
            break
        force_move(direction)

# 4. Make it functions

def get_blocks(locations):
    for loc in locations:
        while True:
            direction = robot.get_location().direction(loc)
            if direction is None:
                break
            force_move(direction)


def lookup(elements):
    for e in elements:
        locations = robot.find_type_nearby(e)
        if len(locations) > 0:
            return locations

# At this point, we have:
# * the list of elements we are looking for
# * the position of those elements if they are closeby
# * A way to go get them
# We need:
# * randomly dig in a direction if nothing is closeby
# * a stop clause to avoid digging forever

import random


def rand_dig(distance=10):
    directions = [Dir.DOWN, Dir.UP, Dir.NORTH, Dir.SOUTH, Dir.EAST, Dir.WEST]
    r_dig = random.choice(directions)

    while robot.move(r_dig):
        distance -= 1

    for i in range(distance):
        robot.mine(r_dig)


def too_far(origin, max_distance=50):
    return (origin.x_coord >= origin.x_coord + max_distance or
            origin.x_coord <= origin.x_coord - max_distance or
            origin.y_coord >= origin.y_coord + max_distance or
            origin.y_coord <= origin.y_coord - max_distance or
            origin.z_coord >= origin.z_coord + max_distance or
            origin.z_coord <= origin.z_coord - max_distance)


def main():
    origin = robot.get_location()
    while not too_far(origin, 50):
        locations = lookup(elements)
        if locations is None or len(locations) == 0:
            rand_dig(5)
            continue
        get_blocks(locations)
        robot.get_inventory()

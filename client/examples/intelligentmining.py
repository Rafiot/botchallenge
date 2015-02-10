#!/usr/bin/env python
# -*- coding: utf-8 -*-


from botchallenge import Robot
from botchallenge import BlockType
from botchallenge import Dir
import random


USERNAME = "rafi0t"  # Put your minecraft username here
SERVER = "localhost"  # Put the address of the minecraft server here
robot = Robot(USERNAME, SERVER)

elements = [BlockType.DIAMOND, BlockType.GOLD_ORE, BlockType.IRON_ORE,
            BlockType.COAL_ORE]


def force_move(direction):
    if robot.is_block_solid(direction):
        robot.mine(direction)
    robot.move(direction)


def lookup(elements):
    for e in elements:
        locations = robot.find_type_nearby(e)
        if len(locations) > 0:
            return locations
    return None


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


def goto(location):
    while True:
        direction = robot.get_location().direction(location)
        if direction is None:
            break
        force_move(direction)


def get_blocks(locations):
    for loc in locations:
        goto(loc)


if __name__ == "__main__":

    origin = robot.get_location()
    while not too_far(origin, 10):
        locations = lookup(elements)
        if locations is None:
            rand_dig(5)
            continue
        get_blocks(locations)
        robot.get_inventory()
    goto(origin)

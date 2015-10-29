#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from botchallenge import Robot

USERNAME = "rafiot"  # Put your minecraft username here
SERVER = "europe.botchallenge.net"  # Put the address of the minecraft server here


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.robot = Robot(USERNAME, SERVER)

    def test_simple(self):
        me = self.robot.get_location()
        owner = self.robot.get_owner_location()
        print(me.distance(owner))

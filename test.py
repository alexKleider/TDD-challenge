#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'test.py'
""" Test code.py  """

import unittest
import code

class CodeTester(unittest.TestCase):
    def setUp(self):
        self.s = code.FooBar()

    def set_up(self):
        print("set_up is running")
        self.s = code.FooBar()

    def SetUp(self):
        print("SetUp is running")
        self.assertTrue(self.s.text == 'Hello, Gang!')

    def TearDown(self):
        print("TearDown is running")

    def tear_down(self):
        print("tear_down is running")

    def TestSomethingCool(self):
        print("TestSomethingCool is running")

    def test_something_cool(self):
        print("test_something_cool is running")

    def ReallyCoolTest(self):
        print("ReallyCoolTest is running")

    def really_cool_test(self):
        print("really_cool_test is running")

    def test_bar(self):
        self.assertTrue(self.s.bar() == "Hello, Bar.")


if __name__ == "__main__":
    unittest.main()


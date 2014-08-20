#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'test.py'
""" Test code.py  """

import unittest
import code

class CodeTester(unittest.TestCase):

    counter_dic = {}

    def setUp(self):
        print("setUp is running")
        CodeTester.counter_dic['setUp'] = \
                            CodeTester.counter_dic.setdefault('setUp', 0) + 1
        self.s = code.FooBar()

    def set_up(self):
        print("set_up is running")
        CodeTester.counter_dic['setup'] = \
            CodeTester.counter_dic.setdefault('setup', 0) + 1
        self.s = code.FooBar()

    def SetUp(self):
        print("SetUp is running")
        CodeTester.counter_dic['SetUp'] = \
                            CodeTester.counter_dic.setdefault('SetUp', 0) + 1
        self.assertTrue(self.s.text == 'Hello, Gang!')

    def tearDown(self):
        print("tearDown is running")

    def tear_down(self):
        print("tear_down is running")
        CodeTester.counter_dic['tear_down'] = \
                        CodeTester.counter_dic.setdefault('tear_down', 0) + 1

    def TestSomethingCool(self):
        print("TestSomethingCool is running")
        CodeTester.counter_dic['TestSomethingCool'] = \
                CodeTester.counter_dic.setdefault('TestSomethingCool', 0) + 1

    def test_something_cool(self):
        print("test_something_cool is running")
        CodeTester.counter_dic['test_something_cool'] = \
                CodeTester.counter_dic.setdefault('test_something_cool', 0) + 1

    def ReallyCoolTest(self):
        print("ReallyCoolTest is running")
        CodeTester.counter_dic['ReallyCoolTest'] = \
                    CodeTester.counter_dic.setdefault('ReallyCoolTest', 0) + 1

    def really_cool_test(self):
        print("really_cool_test is running")
        CodeTester.counter_dic['really_cool_test'] = \
                CodeTester.counter_dic.setdefault('really_cool_test', 0) + 1

    def test_bar(self):
        self.assertTrue(self.s.bar() == "Hello, Bar.")
        CodeTester.counter_dic['assertTrue'] = \
                    CodeTester.counter_dic.setdefault('assertTrue', 0) + 1


if __name__ == "__main__":
    unittest.main()
    for key in CodeTester.counter_dic.keys():
        print("'{0}' was run {1} times.".format(key,
                                            CodeTester.counter_dic[key]))


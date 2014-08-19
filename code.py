#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'code.py'

class FooBar(object):
    def __init__(self):
        self.text = "Hello, World!"

    def hello(self):
        return self.text

    def foo(self):
        return "Hello, Foo."

    def bar(self):
        return "Hello, Bar."

if __name__=="__main__":
    pass


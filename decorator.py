#!/usr/bin/env python

import sys

def execute(fn):
    def wrapper(*args, **kwargs):
        if len(sys.argv) > 1:
            method, params = sys.argv[1], sys.argv[2:]
            modulename = sys.modules[fn.__module__]
            methods = dir(modulename)
            if method in methods:
                print(method)
            return fn()
    return wrapper
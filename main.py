#!/usr/bin/env python

from decorator import *

# some function
def some(params, foo=123, baz='bar'):
    print(foo)
    print("This is some function with param: {}".format(params))
    
# other function
def other():
    print("This is other function")

# main function
@execute
def main():
    print("This is main function")

if __name__ == "__main__":
    main()
    
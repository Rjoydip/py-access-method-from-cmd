#!/usr/bin/env python

import sys

# params function
def params(*kwargs):
    print(*kwargs)
    print("This is params function with param: {}".format(*kwargs))
    
# other function
def other():
    print("This is other function")

# main function
def main():
    print("This is main function")

if __name__ == "__main__":
    options = {
        "main": main,
        "other": other,
        "params": params
    }
    command, params = sys.argv[1], sys.argv[2:]
    options[command](*params)
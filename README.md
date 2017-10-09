# py-method-cmd
> Run python method from command line

# Install locally

```sh
$ git clone https://github.com/Rjoydip/py-delay-decorator.git # clone or fork
$ cd py-delay-decorator
$ python ./main.py
```

## Simpler implementation

Let's start with a simple implementation:

#### Example 1

Without decorator

```python
#!/usr/bin/env python

import sys

# something function
def something():
    print("This is something function")
    
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
        "something": something
    }
    if len(sys.argv) > 1:
        command, params = sys.argv[1], sys.argv[2:]
        options[command](*params)
```

#### Example 2

Using decorator

```python
#!/usr/bin/env python

from decorator import *

# some function
def some(params):
    # print("This is some function")
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
```
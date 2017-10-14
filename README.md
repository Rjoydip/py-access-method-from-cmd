# py-hack-methods

> Access/Hack all python methods from command line

# Install locally

```sh
$ git clone https://github.com/Rjoydip/py-hack-methods.git # clone or fork
$ cd py-hack-methods
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
def some(params, foo=123, baz='bar'):
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

#### def method_name(params[,args])

If value pass form command line then it will get in 1st argumetns(`params`). If default arguments passes in method that can get 2nd arguments onwords, also method can pass `n` terms of arguments.

#### Command

```sh
$ python ./main.py some -p 10
```
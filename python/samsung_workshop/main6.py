import inspect
from functools import wraps
'''
class foo:
  foo class
  print("foo")

class bar:
  ar class
  print("bar")

 fo=foo()
 ba=bar()

 fo
 ba
'''

def logit(func):
    def wrapper(*args,**kwargs):
        print("started ()".format(func.__name__))
        return_value=func(*args,**kwargs)
        print("finished ()".format(func.__name__))
        return return_value
    return wrapper

class foo:
    def met():
        '''foo class'''
    print("foo")

@logit
def foo():
    '''doc'''
    print("foo")

foo()

a=foo()

@logit
def a.met()

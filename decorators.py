# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:22:23 2018

@author: ihassan1
"""

from functools import wraps

def another_function(func):
    @wraps(func)
    def wrapper():
        val = "the result of %s is %s" %(func(),eval(func()))
        
        return val
    return wrapper

@another_function
def a_function():
    """a useless function"""
    return("1+1")

if __name__ == "__main__":
    #a_function()
    print (a_function.__name__)
    print (a_function.__doc__)
    print(a_function())
import functools


#decorator with no arguments
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func(*args, **kwargs): #need to add args and kwargs
        print("in the decorator")
        func(*args, **kwargs) #this is the original function, dont forget to add args and kwargs
        print("after the decorator")
    return function_that_runs_func

@my_decorator
def my_function(x,y):
    print(x+y)

my_function("hello ", "Ish")

#decorators that can accepts arguments themselves
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*arg, **kwargs): #args and kwargs needed to pass in arguments to original function
            print("in the decorator")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

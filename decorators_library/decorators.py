# implement your decorators here.
# """
# timeout decorator

# Useful to given functions a certain max time for execution. The decorator is suppose to track the execution time and raise and exception if the time exceeds given timeout range. Example:

# @timeout(1)
# def very_slow_function():
#     time.sleep(2)

# >>> very_slow_function()
# TimeoutError: Function call timed out
# debug decorator

# This decorator is suppose to debug the executions of the decorated function by logging a message before starting the execution including given params, and a second message after the execution is finished with the returned result. Example:

# @debug()
# def my_add(a, b):
#     return a + b

# >>> my_add(1, 2)
# Executing "my_add" with params: (1, 2), {}
# Finished "my_add" execution with result: 3
# 3
# count_calls decorator

# Keeps track of how many times certain function was called. Example:

# @count_calls
# def my_func():
#   pass

# >>> my_func()
# >>> my_func()
# >>> my_func()
# >>> my_func()
# >>> my_func.counter()
# 4
# memoized decorator

# This decorator should keep track of previous executions of the decorated function and the result of the invokations. If the decorated function is execution again using the same set of arguments sent in the past, the result must be immediately returned by an internal cache instead of re executing the same code again. Example:

# @memoized
# def add(a, b):
#     return a + b

# >>> add(1, 2)
# 3
# >>> add(2, 3)
# 5
# >>> add(1, 2)
# 3  # `add` was not executed, result was returned from internal cache
# """
class debug(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])
            
    def __call__(self, function):
        def wrapper(*args, **kwargs):
            print ('Executing "{}" with params: {}{}'.format(function.__name__, args, kwargs))
            result = function(*args, **kwargs)
            print('Finished "{}" execution with result: {}'.format(function.__name__, result))
        return wrapper

# @debug()
# def my_add(a, b):
#     return a + b

# my_add(1,2)


# Useful to given functions a certain max time for execution. The decorator is suppose to track the execution time and raise and exception if the time exceeds given timeout range. Example:
# import signal
# import time
# import exceptions

class timeout(object):
    def __init__(self, timeout):
        self.timeout = timeout
    def __call__(self, function):
        def sig_handler(signum, frame):
            raise TimeoutError('youslow!!')
        def wrapper():
            signal.signal(signal.SIGALRM, sig_handler)
            signal.alarm(self.timeout)
            result =  function()
            return result
        return wrapper


# @timeout(1)
# def very_slow_function():
#     time.sleep(0)


# very_slow_function()

# # TimeoutError: Function call timed out

# def sig_handler(signum, frame): # those are the arguments passed to the handler always
#   print("Time is now {}".format(str(datetime.datetime.now())))
#   print("Signum:{}\nFrame:{}".format(str(signum), str(frame)))

# signal.signal(signal.SIGALRM, sig_handler)

# print("Time is now {}".format(str(datetime.datetime.now())))
# signal.alarm(5)
# print("Setting alarm")

# class count_calls(object):
#     def __init__(self):
#         self.count = 0
    
#     def __call__(self, function):
#         def wrapper():
#             self.count += 1
#             result = function()
#             return counter()
#         return wrapper
    
#     def counter(self):
#         return self.count

def count_calls(function):
    global count
    count = 0
    def wrapper(*args, **kwargs):
        def counter(count):
            count += 1
            return count
        result = function(*args, **kwargs)
        return result
    return wrapper


@count_calls
def my_func():
    
  print('hello')


my_func()
my_func()
my_func()
my_func().counter()

# This decorator should keep track of previous executions of the decorated function and the result of the invokations. If the decorated function is execution again using the same set of arguments sent in the past, the result must be immediately returned by an internal cache instead of re executing the same code again. Example:

# @memoized
# def add(a, b):
#     return a + b

# >>> add(1, 2)
# 3
# >>> add(2, 3)
# 5
# >>> add(1, 2)
# 3  # `add` was not executed, result was returned from internal cache
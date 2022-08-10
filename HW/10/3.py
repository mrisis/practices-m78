import functools
import time
from functools import cache
import logging

logging.basicConfig()
_logging_level = logging.DEBUG
_logger = logging.getLogger(__name__)
_logger.setLevel(_logging_level)


# __________________________

def process_timer(func):
    @functools.wraps(func)
    def wapper(n):
        start_time = time.time()
        func(n)
        end_time = time.time()
        print(f"time : {end_time - start_time}")

    return wapper


# _______________
def cache1(func):
    caches = {}

    def wrapper(*args):

        signature = (func, args)

        _logger.debug("using singnature:", signature)
        if signature in caches:
            _logger.debug("retrieving  from cache :", signature)
            result = caches[signature]
        else:
            _logger.debug("calculating :%s", signature)
            result = func(*args)
            _logger.debug("caching : %s", signature)
            caches[signature] = result
        return result

    return wrapper


# _____________________
# from functools import wraps

# import time


# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         "inner deco"
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
#         return result
#
#     return timeit_wrapper

# ________________________


# @process_timer
# @timeit
# @cache
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


@process_timer
# @cache
@cache1
def fac(n):
    for i in range(n):
        recur_factorial(n)


# @process_timer
# @timeit
# @cache
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


@process_timer
# @cache
@cache1
def fib(n):
    for i in range(n):
        recur_fibo(i)


# _________________________________
# start_time=time.time()
# print(recur_factorial(9))
# end_time=time.time()
# print(f"time : {end_time - start_time}")


#
# start_time=time.time()
# print(recur_fibo(20))
# end_time=time.time()
# print(f"time : {end_time - start_time}")
# _________________________________________


# print(recur_factorial(90))
# fib(30)
fac(400)

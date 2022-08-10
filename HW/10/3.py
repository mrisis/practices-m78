
import  functools
import time

def process_timer(func):
    @functools.wraps(func)
    def wapper(n):
        start_time= time.time()
        func(n)
        end_time=time.time()
        print(f"time : {end_time - start_time}")

    return wapper


#_____________________
from functools import wraps
from functools import cache
import time


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

#________________________


# @process_timer
# @timeit
# @cache
def recur_factorial(n):

    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)

@process_timer
@cache
def fac(n):
    for i in range(n):
        recur_factorial(n)






@process_timer
# @timeit
# @cache
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


@process_timer
@cache
def fib(n):
    for i in range(n):
        recur_fibo(i)




#_________________________________
# start_time=time.time()
# print(recur_factorial(9))
# end_time=time.time()
# print(f"time : {end_time - start_time}")



#
# start_time=time.time()
# print(recur_fibo(20))
# end_time=time.time()
# print(f"time : {end_time - start_time}")
#_________________________________________


# print(recur_factorial(90))
# fib(20)
fac(400)
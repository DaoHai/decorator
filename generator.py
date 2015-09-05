import time
import functools
import numpy as np

def listize(func):
    def wrapper(*args):
        out = list(func(*args))
        return out
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

def arrayize(func):
    def wrapper(*args):
        out = np.asarray(list(func(*args)))
        return out
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

def lucky_numbers(n):
    ans = []
    for i in range(n):
        if i % 7 != 0:
            continue
        if sum(int(digit) for digit in str(i)) % 3 != 0:
            continue
        ans.append(i)
    return ans

@arrayize
def gen_lucky_numbers(n):
    for i in range(n):
        if i % 7 != 0:
            continue
        if sum(int(digit) for digit in str(i)) % 3 != 0:
            continue
        yield i
        

for i in lucky_numbers(500):
    print(i)


for i in gen_lucky_numbers(500):
    print(i)


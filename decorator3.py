import time
import functools

def timeit(func):
    def wrapper(*args, **kwargs):
        start =  time.time()
        out = func(*args, **kwargs)
	end = time.time()
        print(func.__name__  + " took " + str(end-start) + 's')
        return out
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

def cached(func):
    _cache = {}
    def wrapper(*args, **kwargs):
        try:
	    if args not in _cache: 
                _cache[args] = func(*args, **kwargs)
                return _cache[args]
        except TypeError:
            # ...
        	return func(*args, **kwargs)
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

@cached
def f(x): print('here')

@cached
@timeit
def factorial(n):
    if n <= 1:
        print("computing !")
        return 1
    else:
        return n * factorial(n-1)

#factorial(180)
#factorial(180)
#factorial(180)


f({})
f({})
f({})
f({})
f(1)
f(1)
f(1)
f(1)




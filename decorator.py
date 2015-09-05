import functools

def logger(func):
	
    def wrapper(*args, **kwargs):
        print(func.__name__  + " is called with args " + str([arg for arg in args]) + " kwargs " + str(kwargs))
        out = func(*args, **kwargs)
        print(func.__name__  + " returns " + str(out))
        return out
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper



@logger         
def g(x):
    return 2 * x
 
@logger
def f(x, y):
    return g(x) + g(y)


f(5, 6)


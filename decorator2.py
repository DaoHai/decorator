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

@timeit
def loooong():
    time.sleep(1e-18)
    return 'ans'

loooong()

import time
import functools
from contextlib import contextmanager

def timeit(func):
    def wrapper(*args, **kwargs):
        start =  time.time()
        out = func(*args, **kwargs)
	end = time.time()
        print(func.__name__  + " took " + str(end-start) + 's')
        return out
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

@contextmanager
def longtime_cm():
    start =  time.time()
    yield
    end = time.time()
    print ("it took " + str(end-start) + 's')


@timeit
def loooong():
    time.sleep(3)
    return 'ans'



with longtime_cm():
    time.sleep(3)

loooong()

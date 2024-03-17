import time 
#define a decorator that returns the time the wrapped functions needs to execute
def timemeasure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_took = end_time - start_time
        print(f"function took {time_took} to run")
        return result
    return wrapper
@timemeasure
def sleep():
    time.sleep(2)
sleep()
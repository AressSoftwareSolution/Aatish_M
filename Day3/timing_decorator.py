import time


def timing_decorator(func):
    def wrapper():
        start = time.time()        
        func()                     
        end = time.time()          
        print("Time taken:", end - start, "seconds")
    return wrapper



@timing_decorator
def slow_function():
    time.sleep(2)                 
    print("Function finished")



slow_function()

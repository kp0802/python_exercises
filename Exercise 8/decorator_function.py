import time

def time_this(func):
    def wrapper():
        print(f"Going to execute {func.__name__} function!")
        start_time = time.time()
        result = func()
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"{func.__name__} ran in {time_taken:.8f} seconds!\n\n")
        return result
    return wrapper

@time_this
def slow_function():
    time.sleep(10)
    print("I'm reaaaly slow.....")

@time_this
def fast_function():
    time.sleep(5)
    print("I'm a bit more faster than the above function")

@time_this
def very_fast_function():
    print("I'm the fastest!!")

slow_function()
fast_function()
very_fast_function()
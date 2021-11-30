import time

def time_decorator(func):
    def wrapper():
        starttime = time.time()
        result = func()
        duration = time.time() - starttime
        print(int(duration))
        return result
    return wrapper

@time_decorator
def sleep_1_sec():
    time.sleep(5)
    print("function")
    return 25

result = sleep_1_sec()

print(result)
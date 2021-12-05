# from contextlib import contextmanager
import time

class Timer(object):
    def __init__(self, name):
        self.__name = name
        self.__start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print("EXCEPTION")
        else:
            print(self.__name, int(time.time() - self.__start_time))
        return True

    def sleep(self, sec):
        # print(int(sec))
        time.sleep(sec)

with Timer("perfect_timer") as timer:
    timer.sleep(4)  # этот код будет исполняться 4 секунды
    print("code ended")

with Timer("perfect_timer") as timer:
    raise Exception
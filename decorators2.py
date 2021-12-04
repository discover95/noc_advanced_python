from functools import wraps
import inspect
import datetime

def logging_decorator(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            call_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            log_item = {'name': func.__name__,
                        'arguments': inspect.getcallargs(func, *args, **kwargs),
                        'call_time': call_time,
                        'result': result
                        }
            logger.append(log_item)
            #
            return result
        return wrapper
    return decorator

logger = []  # этот словарь будет хранить наш "лог"

@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127

test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
                # информацией о вызове функции

print(logger)
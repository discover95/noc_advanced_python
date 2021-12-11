class Caller():
    def __init__(self, *args, **kwargs):
        self._functions = list()
        self.counter = 0
        self._args, self._kwargs = args, kwargs

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self._functions):
            return self._functions[self.counter - 1](*self._args, **self._kwargs)
        else:
            raise StopIteration

    def add(self, func):
        self._functions.append(func)

def register_function(caller):
    def decorator(func):
        caller.add(func)
        return func
    return decorator


caller1 = Caller(1, 2, z=5)  # создаем один объект Caller'а, который хранит в себе числовые аргументы
caller2 = Caller('a', 'b', z='c')  # создаем другой объект, со строковыми аргументами

@register_function(caller1)  # регистрируем функцию в обоих объектах
@register_function(caller2)
def summator(x, y, z):       # сама функция просто возвращает сумму аргументов
    return x + y + z

@register_function(caller1)  # только в caller1 зарегистрируем еще одну функцию,
def multiplier(x, y, z):     # которая просто выводит аргументы на экран
    return x * y * z

print(caller1._functions)
print(caller2._functions)

for result in caller1:       # теперь будем лениво вызывать функции, зарегистрированные
    print(result)            # в caller1, выводя их результаты на экран

for result in caller2:       # а теперь лениво вызываем функции, зарегистрированные в caller2
    print(result)

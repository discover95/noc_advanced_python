#Python. Продвинутый курс. НОЦ


##1. Декораторы 1

Ограничение времени 	10 секунд
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

В первом задании курса предлагается решить классическую задачу с собеседований по питону - написать декоратор, который вычисляет время выполнения оборачиваемой функции. Итак, требования к декоратору:
* декоратор должен называться time_decorator
* он должен вычислять время в секундах, в течение которого выполняется обернутая функция при ее вызове. Количество секунд должно быть выведено сразу после выполнения оборачиваемой функции
* после оборачивания функция должна возвращать тот же результат, который возвращала исходная функция
* пробрасывать аргументы из декоратора в функцию необязательно для выполнения этого задания

####Пример использования декоратора
```python
@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25

result = sleep_1_sec()
```
    function
    1
```python
print(result)
```
    25

##2. Декораторы 2
Ограничение времени 	1 секунда
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

В этом задании требуется написать фабрику декораторов, которые будут логировать вызовы функций. Чтобы не усложнять, в качестве журнала событий будем использовать списки. Требования к фабрике:

* фабрика должна называться logging_decorator
* при создании декоратора фабрика должна принять требуемый список-логгер в аргументах
* обернутая функция должна возвращать тот же результат, который бы вернула оборачиваемая функция
* при вызове обернутой функции в список-логгер должен добавляться словарь, в котором будут храниться название функции, список поданных аргументов, время вызова функции и результат, который она вернула. Формат словаря должен быть таким:

{
    'name': 'test_function',
    'arguments': {'a': 1, 'b': 2},
    'call_time': datetime.datetime(2021, 8, 1, 18, 18, 7, 849184),
    'result': 127
}

Ниже приведен пример использования такого декоратора.
Пример использования декоратора

```python
logger = []  # этот словарь будет хранить наш "лог"

@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127

test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
                # информацией о вызове функции

print(logger)
```

    [{'name': 'test_simple', 'arguments': {'a': 1, 'b': 2}, 'call_time': datetime.datetime(2021, 8, 1, 18, 18, 7, 849184), 'result': 127}]

####Примечания

Для удобного получения переданных в функцию аргументов при ее вызове можно использовать функцию getcallargs из модуля inspect. Но стоит учесть, что она так или иначе выполняет вызов исследуемой функции, поэтому такой способ плох, если функция изменяет какие-то глобальные состояния. В тестах к этому заданию таких функций нет, поэтому можно попрактиковаться в использовании модуля inspect.


##3. Контекстный менеджер
Ограничение времени 	10 секунд
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

Вернемся к задачам по профилированию кода, а точнее, по замерам времени его исполнения. В первой задаче контеста вы написали декоратор, которым можно обернуть функцию, и мы узнаем, сколько времени она будет исполняться. Но что если мы не хотим оборачивать профилируемый кусок кода в функцию, но всё равно хотим замерить время его исполнения? Для этой цели напишем контекстный менеджер. Требования к нему будут следующими:

* класс контекстного менеджера должен называться Timer
* в конструкторе мы должны иметь возможность задать название для лога записей о продолжительности исполнения кода (просто строковый аргумент, значение которого нужно запомнить внутри объекта Timer)
* отсчет времени должен начинаться с момента входа в контекстный менеджер
* по завершении исполнения блока кода контекстного менеджера на экран должно быть выведено название таймера и количество секунд, которое исполнялся блок кода, через пробел
* если в коде, который исполняется внутри контекстного менеджера, возникает исключение, на экран выводится "EXCEPTION" (заглавными буквами, без названия таймера)

####Пример использования
```python
with Timer("perfect_timer") as timer:
    timer.sleep(4)  # этот код будет исполняться 4 секунды
    print("code ended")
```
    code ended
    perfect_timer 4

```python
with Timer("perfect_timer") as timer:
    raise Exception
```
    EXCEPTION
    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    Exception


##4. Итератор
Ограничение времени 	1 секунда
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

Допустим, у нас есть ряд функций, которые нам нужно вызывать с одними и теми же аргументами. Для этого мы можем завести сущность (объект), которая будет хранить внутри себя список функций и список параметров. Дальше эта сущность должна вызывать по очереди каждую из функций с параметрами из внутреннего списка и возвращать результат. Реализуем эту сущность в виде итерируемого объекта, к которому предъявляются следующие требования:

* класс, который описывает нашу сущность, должен называться Caller
* в конструкторе он принимает произвольное количество порядковых и именованных аргументов, которые потом нужно передать в функции
* при инициализации объекта список функций внутри него не должен содержать ни одну функцию
* должен быть способ зарегистрировать новую функцию внутри этого объекта

Для того, чтобы было удобней использовать наш Caller в коде, опишем также фабрику декораторов, которая будет регистрировать оборачиваемую функцию в объекте Caller'а, который будет передан фабрике в единственном аргументе. Требования к этой фабрике:

* фабрика декораторов должна называться register_function
* в единственном аргументе фабрика принимает уже созданный объект класса Caller
* после оборачивания функции декоратором из фабрики она должна попасть в список функций переданного объекта класса Caller
* поведение функции не должно измениться после оборачивания
* и register_function, и Caller должны быть описаны в одном файле

####Пример использования
```python
caller1 = Caller(1, 2, z=5)  # создаем один объект Caller'а, который хранит в себе числовые аргументы
caller2 = Caller('a', 'b', z='c')  # создаем другой объект, со строковыми аргументами

@register_function(caller1)  # регистрируем функцию в обоих объектах  
@register_function(caller2)
def summator(x, y, z):       # сама функция просто возвращает сумму аргументов
    return x + y + z

@register_function(caller1)  # только в caller1 зарегистрируем еще одну функцию,
def multiplier(x, y, z):     # которая просто выводит аргументы на экран
    return x * y * z

for result in caller1:       # теперь будем лениво вызывать функции, зарегистрированные
    print(result)            # в caller1, выводя их результаты на экран
```
    8 # выполнилась summator(1, 2, z=5)

    10 # выполнилась multiplier(1, 2, z=5)
```python
for result in caller2:       # а теперь лениво вызываем функции, зарегистрированные в caller2
    print(result)
```
    abc # выполнилась summator('a', 'b', z='c')


##5. Эмуляция контейнеров
Ограничение времени 	10 секунд
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

Напишем свой аналог листа таблицы Excel. Нужно написать структуру данных Field, в которой доступ к значениям будет осуществляться по ключам. Ключом будет пара "буква" - "число", по аналогии с адресом ячейки в Excel. Возможные форматы обращения к одной и той же "ячейке" данных:

```python
field = Field()
field[1, 'a'] = 25
field['a', 1] = 25
field['a', '1'] = 25
field['1', 'a'] = 25
field['1a'] = 25
field['a1'] = 25
field[1, 'A'] = 25
field['A', 1] = 25
field['A', '1'] = 25
field['1', 'A'] = 25
field['1A'] = 25
field['A1'] = 25
```

В этом списке каждая из этих строк записывает число 25 в ячейку с одним и тем же ключом. Соответственно, по любому из перечисленных ключей должно быть можно получить это число из объекта field. Также должны быть реализованы удаление элемента из структуры (через оператор del) и возможность использования оператора in, например:

* (1, 'a') in field: True
* "A1" in field: True
* ('D', '4') in field: False

Таким образом, выходит, что ключом структуры может быть либо кортеж, либо строка. При попытке получить или записать значение по ключу другого типа должно быть вызвано исключение TypeError. При некорректном значении строки или элементов кортежа нужно вызывать исключение ValueError. Корректными значениями будет считать одиночные буквы и неотрицательное целое число любой длины, т.е. правильные варианты ключей:

* А1
* А222543
* Z89

Неправильные варианты ключей:

 *   AA5
 *   Q2.5
 *   -6F
 *   A
 *   27
 *   GG

Кроме вышеперчисленного, по объекту должно быть возможно итерироваться. При проходе циклом по объекту должны возвращаться значения, хранящиеся в нём. Порядок возврата значений не важен.

####Примечания
В своем решении этого задания я использовал в качестве ключей хранимого словаря frozenset, а проверку на ValueError реализовал через регулярку. Также рекомендую проверку типов и преобразование поступившего ключа в тот вид, в котором он хранится "под капотом", вынести в отдельный метод и вызывать его из всех описываемых магических методов.

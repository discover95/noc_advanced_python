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

##6. Дескрипторы
Ограничение времени 	10 секунд
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

Предположим, что нам нужно хранить некоторые числа внутри абсолютно разных объектов. Но также нужен способ сразу все эти числа обратить в 0 одной командой. Для примера, представим, что у нас есть класс, который описывает спортивную команду, и в объекте этого класса хранится текущее количество очков в игре. Когда мы начинаем новую игру, у всех команд количество очков должно стать нулём. Такой функционал можно реализовать, написав дескриптор данных, к которому будут предъявляться следующие требования:

*    название класса-дескриптора - Nuller
*    инициализация дескриптора внутри класса выглядит так: class Team: score = Nuller()
*    при присвоении нового значения в поле-дескриптор score объекта team = Team() это значение сохраняется внутри объекта team
*    при получении значения из поля-дескриптора score объекта team = Team() это значение берется из объекта team
*    класс Nuller содержит метод класса null, который присваивает 0 во все поля-дескрипторы объектов-владельцев. Для этого проще всего внутри класса Nuller хранить ссылки на все объекты-владельцы этого дескриптора
*    при удалении значения из объекта-владельца (с помощью оператора del) удаляется и ссылка из класса Nuller на этот объект

#### Пример использования
```python
class Team:
    score = Nuller()

team1 = Team()
team2 = Team()
team1.score = 5
print(team1.score)
```
    5
```python
team2.score = 28
print(team2.score)
```
    28
```python
Nuller.null()
print(team1.score, team2.score)
```
    0 0
```python
team1.score = 10
del team2.score
Nuller.null()
print(team1.score)
```
    0

####Примечания

Подсказка: для этого нужно хранить внутри дескриптора ссылки на все содержащие его классы и список названий атрибутов, в которых записана ссылка на дескриптор (названия можно получить, например, через __dict__ объекта, сравнив класс атрибута с классом-дескриптором).

##7. Доступ к атрибутам
Ограничение времени 	10 секунд
Ограничение памяти 	64.0 Мб
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt

Доработать класс Field так, чтобы вдобавок к реализованному функционалу появились следующие возможности:

field = Field()

    Запись значения в ячейку:
        field.a1 = 25: эквивалентно field['a1'] = 25
        field.A1 = 25: то же самое

    Получение значения:

      field['b', 2] = 100
      field.b2
      field.B2

    Удаление значения:

        del field.a1, del field.A1 - эквивалентно del field['a', 1]

Таким образом, внутри класса Field методы работы с атрибутами должны работать с тем же объектом, в котором хранятся значения, обрабатываемые в методах __setitem__, __getitem__, __delitem__.

Кроме того, обычное присвоение и получение атрибутов (тех, которые не являются адресом ячейки данных нашего класса) должно производиться по стандартному алгоритму питоновских объектов, т.е. они должны храниться в словаре __dict__ объекта.

```python
field = Field()
field.abcde = 125
print(field.abcde, field.__dict__['abcde'] == 125)
```

    125 True

Для таких атрибутов также должны быть реализованы получение, присваивание и удаление значения.


##8. Асинхронные запросы

Допустим, мы хотим получать информацию из разных источников, и нам нужно убедиться в целостности этой информации. Для того, чтобы сравнить два документа произвольного размера, используется хеширование - преобразование произвольного количества информации в уникальное число/строку.

В этом задании от вас требуется написать функцию count_hash(urls), которая соответствует следующей спецификации:

*    urls - это список http-адресов, на которые нужно отправить запрос и получить ответ
*    внутри функции должна происходить асинхронная отправка запросов по адресам из списка urls и получение ответов. Ответы должны быть отсортированы и сконкатенированы в одну строку. Из полученной строки нужно получить md5-хеш и вернуть его из функции.

Примерный вид функции будет таким:

```python
from hashlib import md5

def count_hash(urls):
    results = <ваш код, который отправляет асинхронные запросы по указанным url-ам>
    s = "".join(sorted(results)).encode('utf-8')
    return md5(s).hexdigest()

```

####Проверка задания

Для проверки задания подготовлены url-ы, которые отвечают на запросы с задержкой в несколько секунд. Подразумевается, что все запросы из функции count_hash будут отправлены параллельно, т.е. суммарное время выполнения этой функции должно равняться максимальной задержке ответа из списка urls. Скрипт проверки проверяет как значение полученного хеша, так и время выполнения функции. Url-ы генерируются случайно, т.е. суммарная задержка в каждом тесте тоже будет случайной.
####Примечания

Данное задание будет проверяться вручную, т.к. система Яндекс.Контест не предоставляет доступ к интернету для кода решений. Самостоятельно вы можете проверить свое решение, используя скрипт, приведенный ниже, где solution - это название файла с вашим решением. Этот же код будет исполнен и при проверке решения.

```python
import time
from random import randint
from hashlib import md5
from solution import count_hash

base_url = "https://nocvko-python.mocklab.io/delayed/"

def test():
    numbers = [randint(1, 8) for _ in range(4)]
    max_time = max(numbers) + 1
    urls = [base_url + str(number) for number in numbers]
    begin = time.time()
    result = count_hash(urls)
    end = time.time()
    assert end - begin < max_time, "Время исполнения запроса превысило ожидание. Вероятно, запросы выполняются не параллельно"
    result_strings = sorted([f"delayed_{i}000" for i in numbers])
    result_string = "".join(result_strings).encode('utf-8')
    assert result == md5(result_string).hexdigest()

if __name__ == "__main__":
    test()
```

####Коды проверки задания

Несмотря на то, что задание проверяется вручную, на этот раз не нужно лично писать преподавателю с просьбой проверить решение. Автоматически при загрузке вы получите статус проверки PE - "частичное решение". Все решения с таким кодом я в течение нескольких дней буду проверять и ставить соответствующий код проверки решения: OK - если решение засчитано, и WA - если в решении есть ошибки. Тех проверок, которые описаны в скрипте выше, достаточно для прохождения тестов, т.е. качество кода дополнительно здесь оцениваться не будет.

##9. Создание библиотеки

При работе с большим количеством данных часто дату хранят в виде строки, а не в формате datetime. Например, `"20210531" - это 31 мая 2021 года. Также очень часто при обработки данных требуются операции, которые прибавляют или убавляют к/от даты какое-то количество дней, месяцев и т.д. Поскольку дата хранится в строке, то для проведения таких операций нужно:

*    привести строку к типу date или datetime
*    прибавить/отнять к/от полученного значения timedelta
*    привести полученную дату обратно к строке, чтобы соблюдался формат данных.

Естественно, каждый раз столько манипуляций проводить не хочется, а стандартная библиотека языка Python не содержит подобный функционал для строк. Давайте напишем библиотеку, в которой опишем необходимые функции для строк!
Требования к названию библиотеки

*    Импортируемый в коде модуль нашей библиотеки должен называться в соответствии с Вашими фамилией и именем. Например, pushkin_alexander. Это означает, что после установки библиотеки ее можно будет использовать в коде, исполнив import pushkin_alexander

*    Название библиотеки в репозитории pypi должно так же называться в соответствии с Вашими фамилией и именем, но с постфиксом _student. Это означает, что установить вашу библиотеку можно будет командой

```pip install pushkin_alexander_student```

###Требования к структуре библиотеки

В нашей библиотеке будет единственный модуль dates.py. Т.е., например, импортировать все функции нашей библиотеки можно будет строкой:

```from pushkin_alexander.dates import *```

где вместо pushkin_alexander будет название вашей библиотеки. Требования к названию библиотеки описаны выше.
Требования к функциям модуля dates

Ниже всегда, когда мы будем говорить о "строке, содержащей дату", будем иметь в виду строку формата "ГГГГММДД". Пример - "20210528".

```    
    def is_date(date: str) -> bool: функция, которая принимает строку и возвращает булевское значение. Если в строке записана валидная дата в формате ГГГГММДД, то возвращается True, иначе False
    def add_days(date: str, days: int) -> str: функция, которая принимает строку, содержащую дату, и количество дней, которое нужно прибавить к этой дате. Количество дней может быть любым целым числом: как положительным, так и отрицательным и нулем. Функция возвращает новую строку, содержащую дату после прибавления количества дней days
    def tomorrow(date: str) -> str: функция, которая принимает строку, содержащую дату, и возвращает строку, содержащую дату следующего после date дня
    def yesterday(date: str) -> str:функция, которая принимает строку, содержащую дату, и возвращает строку, содержащую дату предыдущего перед date дня
    def add_weeks(date: str, weeks: int) -> str: функция, которая принимает строку, содержащую дату, и количество недель, которое нужно прибавить к этой дате. Количество недель может быть любым целым числом: как положительным, так и отрицательным и нулем. Функция возвращает новую строку, содержащую дату после прибавления количества недель weeks. День недели результирующей даты всегда должен совпадать с днем недели исходной даты
    def add_months(date: str, months: int) -> str: функция, которая принимает строку, содержащую дату, и количество месяцев, которое нужно прибавить к этой дате. Количество месяцев может быть любым целым числом: как положительным, так и отрицательным и нулем. Функция возвращает новую строку, содержащую дату после прибавления количества месяцев months. Если в результирующей дате день получается больше, чем количество дней в результирующем месяце, нужно взять последний день этого месяца. Например, 31 мая + 1 месяц = 30 июня, потому что мы должны сдвинуться по календарю на 1 месяц, но в июне всего 30 дней. Также 29 февраля високосного года - 12 месяцев = 28 февраля предыдущего невисокосного года. Однако 30 июня - 1 месяц = 30 мая, поскольку в обратную сторону у нас нет ограничений календаря
    def add_years(date: str, years: int) -> str: функция, которая принимает строку, содержащую дату, и количество лет, которое нужно прибавить к этой дате. Количество лет может быть любым целым числом: как положительным, так и отрицательным и нулем. Функция возвращает новую строку, содержащую дату после прибавления количества лет years. Если в результирующей дате день получается больше, чем количество дней в результирующем месяце, нужно взять последний день этого месяца. Например,29 февраля високосного года + 1 год = 28 февраля следующего невисокосного года
```
Ограничения на использование сторонних библиотек

Вы можете в коде своей библиотеки использовать любые другие библиотеки. Например, в библиотеке для работы с таблицами pandas есть некоторые функции по работе с датами, которые дополняют возможности стандартного модуля datetime. Но учтите, что если вы хотите использовать те модули, которых нет в стандартной библиотеке, вы должны прописать их в аргументах функции setup, чтобы они автоматически установились при установке вашей библиотеки.
Правила отправки решения

*    Загрузите whl вашей библиотеки на nexus курса. Данные для авторизации на нексусе вы можете найти на странице курса в системе moodle (там, где смотрите видео).
*    В форме ответа на это задание напишите в первой строке название pypi-пакета (то, что подавать в pip для установки вашей библиотеки); во второй строке напишите название, под которым можно импортировать вашу библиотеку в интерпретаторе или коде. Если хотите добавить какие-то примечания, напишите их ниже в следующей строке.
*    Так же, как и в предыдущем задании, посылка получит статус PE, и в течение нескольких дней я проверю вашу посылку вручную с помощью скрипта с тестами методов.

####Примечания

Проверить правильность реализации функции вы можете самостоятельно с использованием тестирующего скрипта. Я буду проверять решения тем же скриптом, предварительно выполнив pip install вашей библиотеки.
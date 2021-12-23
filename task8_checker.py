import time
from random import randint
from hashlib import md5
from async_query import count_hash

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
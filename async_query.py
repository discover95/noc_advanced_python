import asyncio
import aiohttp
from hashlib import md5

async def get_response(url):
    async with aiohttp.request('get', url) as response:
        return await response.text()

def count_hash(urls):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for url in urls:
        loop.create_task(get_response(url))
    tasks = asyncio.all_tasks(loop=loop)
    group = asyncio.gather(*tasks, return_exceptions=False)
    results = loop.run_until_complete(group)
    loop.close()

    s = "".join(sorted(results)).encode('utf-8')
    return md5(s).hexdigest()

# print(count_hash(["https://nocvko-python.mocklab.io/delayed/2", "https://nocvko-python.mocklab.io/delayed/1"]))
# print(count_hash(["https://mail.ru", "https://habr.com"]))


def run(url):
    r = yield from aiohttp.request('get', url)
    raw = yield from r.text()
    print(raw)

def sync_count_hash(urls):
    results = []
    for url in urls:
        results.append(asyncio.run(get_response(url)))
    s = "".join(sorted(results)).encode('utf-8')
    return md5(s).hexdigest()

# print(sync_count_hash(["https://nocvko-python.mocklab.io/delayed/2", "https://nocvko-python.mocklab.io/delayed/1"]))
# print(sync_count_hash(["https://mail.ru", "https://habr.com"]))

# def count_hash(urls):
#     results = [x async for x in get_response(urls)]
#     s = "".join(sorted(results)).encode('utf-8')
#     return md5(s).hexdigest()

# async def generator(name, delay, max_):
#     for i in range(max_):
#         yield f"{name}: {i}"
#         await asyncio.sleep(delay)
#
#
# async def run(name, delay):
#     async for i in generator(name, delay, 5):
#         print(i)
#
# async def main():
#     await asyncio.gather(*[run("delay {i}", 3) for i in range(1, 3)])
#
# asyncio.run(main())

async def main():
    print("Request")
    async with aiohttp.request('GET', "https://habr.comm") as response:
        print("status:", response.status)

asyncio.run(main())
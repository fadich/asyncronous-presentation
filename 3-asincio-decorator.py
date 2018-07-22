import asyncio
import aiohttp


@asyncio.coroutine
def read_url(url):
    print('Starting {}'.format(url))

    session = aiohttp.ClientSession()
    response = yield from session.get(url)
    data = yield from response.text()

    print('{}: {} bytes'.format(url, len(data)))

    yield from session.close()

    return data


if __name__ == '__main__':
    urls = ('http://www.python.org', 'https://pypi.org', 'http://google.com')
    futures = [read_url(url) for url in urls]
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(futures))

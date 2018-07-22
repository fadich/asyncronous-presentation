import asyncio
import aiohttp


async def read_url(url):
    print('Starting {}'.format(url))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print('{}: {} bytes'.format(url, len(data)))

    return data


if __name__ == '__main__':
    urls = ('http://www.python.org', 'https://pypi.org', 'http://google.com')
    futures = [read_url(url) for url in urls]
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(futures))


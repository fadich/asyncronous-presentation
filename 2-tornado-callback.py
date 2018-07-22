import tornado.ioloop

from tornado.httpclient import AsyncHTTPClient


def read_url(response):
    if response.error:
        print('Error: ', response.error)
    else:
        url = response.request.url
        data = response.body
        print('{}: {} bytes'.format(url, len(data)))


if __name__ == '__main__':
    urls = ('http://www.python.org', 'https://pypi.org', 'http://google.com')
    http_client = AsyncHTTPClient()

    for url in urls:
        http_client.fetch(url, read_url)

    try:
        instance = tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass

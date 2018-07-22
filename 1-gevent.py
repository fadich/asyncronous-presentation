import gevent.monkey

from urllib.request import urlopen


def read_url(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {} bytes'.format(url, len(data)))


if __name__ == '__main__':
    urls = ('http://www.python.org', 'https://pypi.org', 'http://google.com')
    jobs = [gevent.spawn(read_url, url) for url in urls]

    gevent.monkey.patch_all()
    gevent.wait(jobs)

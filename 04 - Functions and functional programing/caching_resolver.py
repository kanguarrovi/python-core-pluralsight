import socket

class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


if __name__ == '__main__':
    resolve = Resolver()
    print(resolve('sixty-north.com'))

    print(resolve.__call__('sixty-north.com'))

    print(resolve._cache)

    print(resolve('pluralsight.com'))

    print(resolve._cache)

    from timeit import timeit

    print(timeit(setup="from __main__ import resolve", stmt="resolve('google.com')", number=1))

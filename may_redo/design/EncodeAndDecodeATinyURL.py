from random import Random


class Codec:

    def __init__(self):
        self._tiny_url = 'http://tinyurl.com/'
        self._hash_map = {}
        self._random = Random()
        self._alphabets = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._key = self._get_rand()

    def _get_rand(self) -> str:
        key = []
        for _ in range(6):
            key.append(self._random.choice(self._alphabets))
        return ''.join(key)

    def encode(self, long_url: str) -> str:
        while self._key in self._hash_map:
            self._key = self._get_rand()
        self._hash_map[self._key] = long_url
        return self._tiny_url + self._key

    def decode(self, short_url: str) -> str:
        return self._hash_map.get(short_url.replace(self._tiny_url, ''))

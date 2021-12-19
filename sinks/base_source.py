import requests

class BaseSource(object):
    def __init__(self, source):
        self.source = source
        self.funcs = []

    @classmethod
    def from_json_url(cls, url):
        result = requests.get(url)

        return cls(result.json())

    def __rshift__(self, other):
        self.funcs.append(other)

        return self

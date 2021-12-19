import functools
import requests

from sinks.base_source import BaseSource


class Source(BaseSource):
    def __call__(self):
        return functools.reduce(lambda acc, f: f(acc), self.funcs, self.source)

import functools

from sinks.base_source import BaseSource


class GeneratorSource(BaseSource):
    def __init__(self, source):
        self.source = source
        self.funcs = []

    def __iter__(self):
        return (self.__pipe(i) for i in self.source)

    def __pipe(self, item):
        return functools.reduce(lambda acc, f: f(acc), self.funcs, item)

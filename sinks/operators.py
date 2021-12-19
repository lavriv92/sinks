"""
Provides operators
"""
import functools
import itertools


__all__ = ['extract_key', 'extract_partials', 'group_by', 'groupped']


def extract_key(key):
    return functools.partial(map, lambda x: x.get(key, None))


def extract_partials(*keys):
    return functools.partial(map, lambda item: {k: item[k] for  k in keys})


def group_by(key):
    return lambda data: functools.reduce(group_reducer(key), data, {})


def groupped(chunk_size=1):
    def wrapped(iterable):
        l = len(iterable)
        for i in range(0, l, chunk_size):
            yield iterable[i:min(i + chunk_size, l)]

    return wrapped


def group_reducer(key):
    def wrapped(acc, item):
        key_name = item[key]

        if key_name in acc:
            acc[key_name].append(item)
        else:
            acc[key_name] = [item]
        return acc

    return wrapped

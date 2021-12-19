import functools
import itertools


__all__ = ['extract_key', 'extract_partials', 'group_by']


def extract_key(key):
    return functools.partial(map, lambda x: x.get(key, None))


def extract_partials(*keys):
    return functools.partial(map, lambda item: {k: item[k] for  k in keys})


def group_by(key):
    return lambda data: functools.reduce(group_reducer(key), data, {})


def group_reducer(key):
    def wrapped(acc, item):
        key_name = item[key]

        if key_name in acc:
            acc[key_name].append(item)
        else:
            acc[key_name] = [item]
        return acc

    return wrapped

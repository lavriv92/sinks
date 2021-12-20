"""
Provides operators

:meta public:
"""
import functools
import itertools
import collections


__all__ = ['extract_key', 'extract_partials', 'group_by', 'groupped']


def extract_key(key: str):
    """
    Extracts field from element of collections 

    Attributes
    ----------

    key: str

    Returns
    -------
    func
        function to extract specified field using key

    :meta public:
    """
    return functools.partial(map, lambda x: x.get(key, None))


def extract_partials(*keys):
    return functools.partial(map, lambda item: {k: item[k] for  k in keys})


def group_by(key):
    empty_result = collections.defaultdict(list)
    return lambda data: dict(
        functools.reduce(group_reducer(key), data, empty_result)
    )


def groupped(chunk_size=1):
    def wrapped(iterable):
        l = len(iterable)
        return (
            iterable[i:min(i + chunk_size, l)] for i in range(0, l, chunk_size)
        )

    return wrapped


def group_reducer(key):
    def wrapped(acc, item):
        acc[item[key]].append(item)

        return acc

    return wrapped

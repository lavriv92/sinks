"""
Provides operators

:meta public:
"""
import asyncio
import functools
import collections


__all__ = ['extract_key', 
           'extract_partials', 'group_by', 'groupped', 'take', 'take_while']


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
    """
    Exatracts partial object from

    Attributes
    ----------
    *keys list[str]

    Returns
    -------
    func 

    :meta public:
    """
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


def take(n):
    return lambda data: data[:min(n, len(data))]


def async_map(fn):
    async def wrapper(collection):
        tasks = [fn(item) for item in collection]

        return asyncio.gather(*tasks)

    return wrapper


def take_while(func):
    return lambda data: [val for val in data if func(val)]


def group_reducer(key):
    def wrapped(acc, item):
        acc[item[key]].append(item)

        return acc

    return wrapped

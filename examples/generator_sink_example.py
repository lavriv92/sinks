import sys
from pathlib import Path

sys.path.append(str(Path('.').absolute().parent))

import pprint
import functools

from sinks import GeneratorSource
from sinks.operators import extract_key, extract_partials, group_by


def main():
    add_six = lambda x: x + 6
    divide = lambda x: x / 2

    source = (
        GeneratorSource([1,2,3,4])
            >> add_six
            >> divide
    )

    for i in source:
        print(i)

if __name__ == '__main__':
    main()

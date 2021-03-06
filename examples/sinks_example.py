

import sys
from pathlib import Path

sys.path.append(str(Path('.').absolute().parent))

import pprint

from sinks import Source
from sinks.operators import extract_key, extract_partials, group_by, groupped, take_while, take


def main():
    add_six = lambda x: x + 6

    (
        Source(2)
          >> add_six
          >> print
    )()

    (
        Source.from_json_url('https://jsonplaceholder.typicode.com/albums')
            >> extract_partials('id', 'title', 'userId')
            >> group_by('userId')
            >> pprint.pprint
    )()

    (
        Source([1,2,3,4,5,6,7,8,9,10,11,12])
          >> groupped(3)
          >> list
          >> pprint.pprint
    )()

    (
        Source([1,2,3,4,5,6,7,8,9, 0])
          >> take(4)
          >> pprint.pprint
    )()

    (
        Source([1,2,3,4,5,6,7,8])
           >> take_while(lambda i: i <= 5)
           >> pprint.pprint
    )()

if __name__ == '__main__':
    main()

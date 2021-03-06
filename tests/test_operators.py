import unittest

from sinks.operators import (
    extract_key, extract_partials, take, take_while, groupped, group_by
)
from sinks.sink import Source


class OperatorsTestCase(unittest.TestCase):

    def test_extract_key(self):
        source = Source([{'message': 'Test'}])
        r = source >> extract_key('message') >> list

        self.assertEqual(r(), ['Test'])

    def test_extract_partials(self):
        source = Source([{'foo': 'foo', 'bar': 'bar'}])
        r = source >> extract_partials('foo') >> list

        self.assertEqual(r(), [{'foo': 'foo'}])

    def test_take(self):
        source = Source([1,2,3,4])
        r = source >> take(3) >> list

        self.assertListEqual(r(), [1, 2, 3])

    def test_take_while(self):
        source = Source([1,2,3,4,5])
        less_then_3 = lambda x: x < 3
        r = source >> take_while(less_then_3) >> list

        self.assertEqual(r(), [1, 2])

    def test_groupped(self):
        source = Source([1,2,3,4])
        r = source >> groupped(2) >> list

        self.assertEqual(r(), [[1, 2], [3, 4]])

    def test_group_by(self):
        books = [
            {'name': 'Lord of the rings', 'author': 'J. R. R. Tolkin'},
            {'name': 'Harry Potter', 'author': 'J. K. Roling'},
            {'name': 'Fantastic beasts', 'author': 'J. K. Roling'}
        ]
        source = Source(books)
        r = source >> group_by('author')
        expected_result = {
            'J. K. Roling': [
                {'name': 'Harry Potter', 'author': 'J. K. Roling'},
                {'name': 'Fantastic beasts', 'author': 'J. K. Roling'}
            ],
            'J. R. R. Tolkin': [
                {'name': 'Lord of the rings', 'author': 'J. R. R. Tolkin'}
            ]
        }

        self.assertEqual(r(), expected_result)

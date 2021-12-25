import unittest
import functools

from sinks import Source


class SourceTestCase(unittest.TestCase):

    def test_adding_operator(self):
        first_test_operator = lambda x: x + 1
        secod_test_operator = lambda x: x + 2

        source = Source([1, 2, 3])

        source >> first_test_operator >> secod_test_operator

        self.assertEqual(len(source.funcs), 2)

    def test_adding_source(self):
        source = Source([1, 2, 3])

        self.assertListEqual(source.source, [1, 2, 3])

    def test_correct_combinations(self):
        add_one = functools.partial(map, lambda x: x + 1)
        source = Source([1,2,3])
        r = source >> add_one >> list

        self.assertListEqual(r(), [2,3,4])


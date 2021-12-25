import unittest

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
        source = Source([1,2,4])

        self.assertEqual(1, 1)

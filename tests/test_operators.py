import unittest

from sinks.operators import extract_key, extract_partials
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

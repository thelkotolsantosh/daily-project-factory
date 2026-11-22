import unittest
from datetime import timedelta
from factory import START, slots


class Planning(unittest.TestCase):
    def test_recovery(self):
        seen = {(START.isoformat(), "A")}
        self.assertEqual(list(slots(START + timedelta(days=1), "A", seen)), [((START + timedelta(days=1)).isoformat(), "A", "machine learning")])
        self.assertEqual(len(list(slots(START, "B", seen))), 1)

    def test_future_start(self):
        self.assertEqual(list(slots(START - timedelta(days=1), "B", set())), [])

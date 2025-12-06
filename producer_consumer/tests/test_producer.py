import unittest

from src.blocking_queue import BlockingQueue
from src.containers import SourceContainer
from src.producer import Producer


class TestProducer(unittest.TestCase):
    def test_produces_all_items_and_sentinel(self):
        items = list(range(5))
        source = SourceContainer(items)
        q = BlockingQueue(len(items) + 1)  # enough capacity

        producer = Producer(source, q)
        producer.start()
        producer.join()

        seen = []
        while True:
            item = q.get()
            if item is None:
                break
            seen.append(item)

        self.assertEqual(seen, items)

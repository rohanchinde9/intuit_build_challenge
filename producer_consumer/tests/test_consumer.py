from src.blocking_queue import BlockingQueue
from src.containers import DestinationContainer
from src.consumer import Consumer
import unittest


class TestConsumer(unittest.TestCase):
    def test_consume_all_items_until_sentinel(self):
        items = list(range(5))
        q = BlockingQueue(len(items) + 1)  # enough room for all items + sentinel

        for x in items:
            q.put(x)
        q.put(None)  # sentinel

        dest = DestinationContainer()
        consumer = Consumer(q, dest)
        consumer.start()
        consumer.join()

        self.assertEqual(dest.items, items)

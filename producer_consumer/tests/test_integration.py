import unittest

from src.blocking_queue import BlockingQueue
from src.containers import SourceContainer, DestinationContainer
from src.producer import Producer
from src.consumer import Consumer


class TestIntegration(unittest.TestCase):
    def test_full_flow_producer_to_consumer(self):
        source = SourceContainer(list(range(10)))
        dest = DestinationContainer()
        queue = BlockingQueue(3)

        producer = Producer(source, queue)
        consumer = Consumer(queue, dest)

        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

        self.assertEqual(dest.items, source.items)

    def test_empty_source(self):
        source = SourceContainer([])
        dest = DestinationContainer()
        queue = BlockingQueue(2)

        producer = Producer(source, queue)
        consumer = Consumer(queue, dest)

        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

        self.assertEqual(dest.items, [])

import unittest
import threading

from src.blocking_queue import BlockingQueue


class TestBlockingQueue(unittest.TestCase):
    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            BlockingQueue(0)
        with self.assertRaises(ValueError):
            BlockingQueue(-5)

    def test_put_get(self):
        q = BlockingQueue(2)
        q.put(42)
        q.put(99)
        self.assertEqual(q.get(), 42)
        self.assertEqual(q.get(), 99)

    def test_blocking_on_full(self):
        q = BlockingQueue(1)
        q.put("first")

        started = threading.Event()

        def producer_task():
            started.set()
            q.put("second")  # should block until get() frees space

        t = threading.Thread(target=producer_task)
        t.start()
        started.wait(1)
        self.assertTrue(t.is_alive())  # still blocked

        # Free space
        self.assertEqual(q.get(), "first")
        t.join(timeout=1)
        self.assertFalse(t.is_alive())

    def test_blocking_on_empty(self):
        q = BlockingQueue(1)

        started = threading.Event()
        result = []

        def consumer_task():
            started.set()
            item = q.get()  # blocks until put()
            result.append(item)

        t = threading.Thread(target=consumer_task)
        t.start()
        started.wait(1)
        self.assertTrue(t.is_alive())  # still waiting

        q.put("item")
        t.join(timeout=1)
        self.assertFalse(t.is_alive())
        self.assertEqual(result[0], "item")

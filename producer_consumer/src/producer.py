# src/producer.py
import threading
import time
import random
from .blocking_queue import BlockingQueue
from .containers import SourceContainer


class Producer(threading.Thread):
    """
    Producer thread: reads items from a SourceContainer
    and places them into a BlockingQueue.
    """

    def __init__(self, source: SourceContainer, queue: BlockingQueue):
        super().__init__()
        self.source = source
        self.queue = queue

    def run(self) -> None:
        # Use None as a sentinel to signal the consumer to stop (assumes data is never None).
        for item in self.source.items:
            self.queue.put(item)
            print(f"[Producer] Produced: {item}")
            time.sleep(random.uniform(0.05, 0.15))

        # Signal shutdown to consumer(s)
        self.queue.put(None)

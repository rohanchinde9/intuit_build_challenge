# src/consumer.py
import threading
import time
import random
from .blocking_queue import BlockingQueue
from .containers import DestinationContainer


class Consumer(threading.Thread):
    """
    Consumer thread: reads items from a BlockingQueue
    and stores them into a DestinationContainer.
    """

    def __init__(self, queue: BlockingQueue, destination: DestinationContainer):
        super().__init__()
        self.queue = queue
        self.destination = destination

    def run(self):
        while True:
            item = self.queue.get()

            # Sentinel value means producer is finished
            if item is None:
                break

            print(f"[Consumer] Consumed: {item}")
            self.destination.store(item)
            time.sleep(random.uniform(0.05, 0.15))

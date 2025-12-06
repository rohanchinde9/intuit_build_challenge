# src/blocking_queue.py
from __future__ import annotations
from collections import deque
import threading
from typing import Any, List


class BlockingQueue:
    """
    A simple bounded blocking queue for producer-consumer.
    Implements wait/notify for thread synchronization.
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self._capacity: int = capacity
        self._buffer = deque()
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: Any) -> None:
        """Block if the queue is full, otherwise insert item."""
        with self._not_full:
            while len(self._buffer) >= self._capacity:
                self._not_full.wait()

            self._buffer.append(item)
            self._not_empty.notify()

    def get(self) -> Any:
        """Block if the queue is empty, otherwise remove and return an item."""
        with self._not_empty:
            while not self._buffer:
                self._not_empty.wait()

            item = self._buffer.popleft()
            self._not_full.notify()
            return item 

    def size(self) -> int:
        """Current number of items in the queue."""
        with self._lock:
            return len(self._buffer)

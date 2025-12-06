# src/containers.py
from typing import Any, List


class SourceContainer:
    """Holds items for the producer."""
    def __init__(self, items: List[Any]):
        self.items = items


class DestinationContainer:
    """Stores items consumed by the consumer."""
    def __init__(self):
        self.items: List[Any] = []

    def store(self, item: Any) -> None:
        self.items.append(item)

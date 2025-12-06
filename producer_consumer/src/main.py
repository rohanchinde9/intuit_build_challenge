# src/main.py
from .blocking_queue import BlockingQueue
from .containers import SourceContainer, DestinationContainer
from .producer import Producer
from .consumer import Consumer

"""Entry point for the producer-consumer demo using BlockingQueue."""
def main():
    source = SourceContainer(list(range(10)))
    destination = DestinationContainer()

    queue = BlockingQueue(capacity=10)

    producer = Producer(source, queue)
    consumer = Consumer(queue, destination)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("\n=== Summary ===")
    print("Source items:     ", source.items)
    print("Destination items:", destination.items)
    print("All items transferred correctly:",
      source.items == destination.items)



if __name__ == "__main__":
    main()

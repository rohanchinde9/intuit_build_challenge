# Producer–Consumer Blocking Queue (Python)

This project implements the classic producer–consumer pattern in Python using a custom bounded blocking queue and threads. It demonstrates thread synchronization, concurrent programming, blocking queues, and a wait/notify-style mechanism.

## Requirements

- Python 3.11+
- No external dependencies; only Python standard library modules are used (`threading`, `collections`, `unittest`, `typing`)

## Project Structure

### `src/`

- **`blocking_queue.py`** – `BlockingQueue` class implementing a bounded blocking queue using a lock and two condition variables
- **`producer.py`** – Producer thread that reads from `SourceContainer` and enqueues items, then sends a sentinel to signal completion
- **`consumer.py`** – Consumer thread that dequeues items and writes them to `DestinationContainer`, stopping when it receives the sentinel
- **`containers.py`** – `SourceContainer` and `DestinationContainer` classes representing the source and destination of data
- **`main.py`** – Entry point that wires everything together and prints final results to the console

### `tests/` (all using `unittest`)

- **`test_blocking_queue.py`** – Unit tests for queue capacity, FIFO behavior, and blocking on full/empty
- **`test_producer.py`** – Tests that Producer enqueues all items plus the sentinel
- **`test_consumer.py`** – Tests that Consumer consumes all items and stops on the sentinel
- **`test_integration.py`** – End-to-end tests for the full producer–consumer pipeline

## Setup

From the repository root:

```bash
cd producer_consumer
```

## Running the Demo

From the `producer_consumer` folder:

```bash
python -m src.main
```

This:
1. Creates a `SourceContainer` with a sequence of integers
2. Starts a `Producer` and `Consumer` sharing a `BlockingQueue`
3. Waits for both threads to finish
4. Prints the source data, destination data, and verification that they match

### Example Output

```
[Producer] Produced: 0
[Consumer] Consumed: 0
[Producer] Produced: 1
[Consumer] Consumed: 1
[Producer] Produced: 2
[Consumer] Consumed: 2
[Producer] Produced: 3
[Consumer] Consumed: 3
[Producer] Produced: 4
[Consumer] Consumed: 4
[Producer] Produced: 5
[Consumer] Consumed: 5
[Producer] Produced: 6
[Consumer] Consumed: 6
[Producer] Produced: 7
[Consumer] Consumed: 7
[Producer] Produced: 8
[Consumer] Consumed: 8
[Producer] Produced: 9
[Consumer] Consumed: 9

=== Summary ===
Source items:      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Destination items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
All items transferred correctly: True
```

This confirms that every item produced was successfully consumed and transferred from source to destination.

## Running Tests

From the `producer_consumer` folder:

```bash
python -m unittest discover -s tests
```

This runs:
- Unit tests for the blocking queue (including blocking behavior on full/empty)
- Unit tests for producer and consumer logic
- Integration tests for the full pipeline

All tests use Python's built-in `unittest` framework.

## Measuring Test Coverage

You can use `coverage.py` to measure code coverage.

### Install (once, if needed)

```bash
pip install coverage
```

### Run Coverage Analysis

From the `producer_consumer` folder:

```bash
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
```

This prints per-file coverage and highlights any lines not executed by tests.

### Generate HTML Report

```bash
python -m coverage html
```

An HTML report will be generated in the `htmlcov/` directory.
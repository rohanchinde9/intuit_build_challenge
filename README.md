# Intuit Build Challenge

This repository contains two assignments demonstrating different programming concepts in Python:

## Assignments

1. Producer–Consumer Blocking Queue (Python)
   - Folder: `producer_consumer/`
   - Demonstrates thread synchronization, bounded blocking queue, and unit tests.
   - See `producer_consumer/README.md` for setup, tests, and sample console output.

2. Sales Data Analysis (CSV, Python)
   - Folder: `sales_data_analysis/`
   - Performs functional/stream-style aggregations on a Superstore CSV.
   - See `sales_data_analysis/README.md` for setup, tests, and sample console output.

## Assignment 1: Producer–Consumer Blocking Queue

This project implements the classic producer–consumer pattern in Python using a custom bounded blocking queue and threads. It demonstrates thread synchronization, concurrent programming, blocking queues, and a wait/notify-style mechanism.

### Requirements

- Python 3.11+
- No external dependencies; only Python standard library modules are used (`threading`, `collections`, `unittest`, `typing`)

### Project Structure

- `src/`
  - `blocking_queue.py` – `BlockingQueue` class implementing a bounded blocking queue using a lock and two condition variables
  - `producer.py` – Producer thread that reads from `SourceContainer` and enqueues items, then sends a sentinel to signal completion
  - `consumer.py` – Consumer thread that dequeues items and writes them to `DestinationContainer`, stopping when it receives the sentinel
  - `containers.py` – `SourceContainer` and `DestinationContainer` classes representing the source and destination of data
  - `main.py` – Entry point that wires everything together and prints final results to the console

### Setup

From the repository root:

```bash
cd producer_consumer
```

### Running the Demo

From the `producer_consumer` folder:

```bash
python -m src.main
```

#### Example Output

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

### Running Tests

From the `producer_consumer` folder:

```bash
python -m unittest discover -s tests
```

This runs:
- Unit tests for the blocking queue (including blocking behavior on full/empty)
- Unit tests for producer and consumer logic
- Integration tests for the full pipeline

### Measuring Test Coverage

You can use `coverage.py` to measure code coverage.

#### Install (once, if needed)

```bash
pip install coverage
```

#### Run Coverage Analysis

From the `producer_consumer` folder:

```bash
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
```

#### Generate HTML Report

```bash
python -m coverage html
```

An HTML report will be generated in the `htmlcov/` directory.

## Assignment 2: Sales Data Analysis

A compact, easy-to-run utility that analyzes a Superstore-style sales CSV using only the Python standard library. It demonstrates streaming CSV parsing, dataclass modeling, grouping/aggregation, and a top‑N product ranking.

### Requirements

- Python 3.11+
- No external dependencies; only Python standard library modules are used ( `csv`, `dataclasses`, `collections`, `pathlib`, `typing`, `unittest`)

## Project Structure

### `data/`

- **`superstore_sales.csv`** – Superstore-style sales dataset used as the input for all analyses. [web:220]

### `src/`

- **`sales_model.py`** – `Sale` dataclass representing a single CSV row and `read_sales(csv_path)` generator that streams records using the standard `csv` module. [web:233]
- **`sales_analysis.py`** – Pure, functional-style analysis functions for total revenue, group-by aggregations (region, category, segment), and top‑N product ranking.
- **`main.py`** – Entry point that loads the CSV file, invokes the analysis functions, and prints all analysis results to the console.

### `tests/` (all using `unittest`)

- **`test_sales_analysis.py`** – Unit tests for all analysis functions (`total_revenue`, `revenue_by_region`, `revenue_by_category`, `revenue_by_segment`, `top_n_products_by_revenue`). [web:176]


### Setup

From the repository root:

```bash
cd sales_data_analysis
```

### Running the Demo

From the `sales_data_analysis` folder:

```bash
python -m src.main
```

#### Example Output

```
=== Sales Data Analysis ===
Total revenue: 2297200.86

Revenue by region:
  South: 391721.91
  West: 725457.82
  Central: 501239.89
  East: 678781.24

Revenue by category:
  Furniture: 741999.80
  Office Supplies: 719047.03
  Technology: 836154.03

Revenue by customer segment:
  Consumer: 1161401.34
  Corporate: 706146.37
  Home Office: 429653.15

Top 5 products by revenue:
  Canon imageCLASS 2200 Advanced Copier: 61599.82
  Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind: 27453.38
  Cisco TelePresence System EX90 Videoconferencing Unit: 22638.48
  HON 5400 Series Task Chairs for Big and Tall: 21870.58
  GBC DocuBind TL300 Electric Binding System: 19823.48
```

### Tests

Run all unit tests:

```bash
python -m unittest discover -s tests
```

`tests/test_sales_analysis.py` covers all exported analysis functions using in-memory sample data.
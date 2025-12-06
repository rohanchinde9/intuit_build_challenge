# Sales Data Analysis

A compact, easy-to-run utility that analyzes a Superstore-style sales CSV using only the Python standard library. It demonstrates streaming CSV parsing, dataclass modeling, grouping/aggregation, and a top‑N product ranking.

## Requirements

- Python 3.11+
-  No external dependencies; only Python standard library modules are used ( `csv`, `dataclasses`, `collections`, `pathlib`, `typing`, `unittest`)

## Project Structure

### `data/`

- **`superstore_sales.csv`** – Superstore-style sales dataset used as the input for all analyses.

### `src/`

- **`sales_model.py`** – `Sale` dataclass representing a single CSV row and `read_sales(csv_path)` generator that streams records using the standard `csv` module.
- **`sales_analysis.py`** – Pure, functional-style analysis functions for total revenue, group-by aggregations (region, category, segment), and top‑N product ranking.
- **`main.py`** – Entry point that loads the CSV file, invokes the analysis functions, and prints all analysis results to the console.

### `tests/` (all using `unittest`)

- **`test_sales_analysis.py`** – Unit tests for all analysis functions (`total_revenue`, `revenue_by_region`, `revenue_by_category`, `revenue_by_segment`, `top_n_products_by_revenue`).


## Setup

From the repository root:

```bash
cd sales_data_analysis
```

## Running the Demo

From the `sales_data_analysis` folder:

```bash
python -m src.main
```

That command:
1. Streams rows from `data/superstore_sales.csv` into `Sale` objects.
2. Computes total revenue and grouped aggregates (region, category, segment).
3. Lists the top‑N products by revenue (N set in `src/main.py`).
4. Prints results to the console.

## Example output

This is the actual output produced with the repository CSV:

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

(To reproduce, run `python -m src.main` from the sales_data_analysis folder.)

## Running Tests

Run all unit tests:

```bash
python -m unittest discover -s tests
```

`tests/test_sales_analysis.py` covers all exported analysis functions using in-memory sample data.

## Notes & tips

- Functions accept any iterable of `Sale` objects — easy to test with lists.
- For very large CSVs, the code streams rows and aggregates incrementally to avoid high memory use.
- Adjust top‑N value in `src/main.py` to see more or fewer products.


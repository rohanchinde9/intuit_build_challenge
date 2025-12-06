# src/sales_model.py

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterator
import csv


@dataclass(frozen=True)
class Sale:
    row_id: str
    order_id: str
    order_date: str      # keep as string; format not important for our aggregations
    ship_date: str
    ship_mode: str
    customer_id: str
    customer_name: str
    segment: str
    country: str
    city: str
    state: str
    postal_code: str
    region: str
    product_id: str
    category: str
    sub_category: str
    product_name: str
    sales: float
    quantity: int
    discount: float
    profit: float

    @property
    def revenue(self) -> float:
        """
        Treat 'Sales' as the main revenue metric.
        Many Superstore datasets already have discount applied in Sales,
        but this property makes the intent explicit.
        """
        return self.sales


def read_sales(csv_path: Path) -> Iterator[Sale]:
    """Stream Sale records from the given CSV file."""
    with csv_path.open(newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Sale(
                row_id=row["Row ID"],
                order_id=row["Order ID"],
                order_date=row["Order Date"],
                ship_date=row["Ship Date"],
                ship_mode=row["Ship Mode"],
                customer_id=row["Customer ID"],
                customer_name=row["Customer Name"],
                segment=row["Segment"],
                country=row["Country"],
                city=row["City"],
                state=row["State"],
                postal_code=str(row["Postal Code"]),
                region=row["Region"],
                product_id=row["Product ID"],
                category=row["Category"],
                sub_category=row["Sub-Category"],
                product_name=row["Product Name"],
                sales=float(row["Sales"]),
                quantity=int(row["Quantity"]),
                discount=float(row["Discount"]),
                profit=float(row["Profit"]),
            )

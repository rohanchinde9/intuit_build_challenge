# src/main.py

from __future__ import annotations

from pathlib import Path

from .sales_model import read_sales
from .sales_analysis import (
    total_revenue,
    revenue_by_region,
    revenue_by_category,
    revenue_by_segment,
    top_n_products_by_revenue,
)


def main() -> None:
    data_path = (
        Path(__file__).resolve().parent.parent / "data" / "superstore_sales.csv"
    )
    sales_list = list(read_sales(data_path))  # materialize once for reuse

    print("=== Sales Data Analysis ===")

    print(f"Total revenue: {total_revenue(sales_list):.2f}")

    print("\nRevenue by region:")
    for region, rev in revenue_by_region(sales_list).items():
        print(f"  {region}: {rev:.2f}")

    print("\nRevenue by category:")
    for category, rev in revenue_by_category(sales_list).items():
        print(f"  {category}: {rev:.2f}")

    print("\nRevenue by customer segment:")
    for segment, rev in revenue_by_segment(sales_list).items():
        print(f"  {segment}: {rev:.2f}")

    print("\nTop 5 products by revenue:")
    for product, rev in top_n_products_by_revenue(sales_list, 5):
        print(f"  {product}: {rev:.2f}")


if __name__ == "__main__":
    main()
# src/sales_analysis.py
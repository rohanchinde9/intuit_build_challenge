# tests/test_sales_analysis.py
"""
Unit tests for sales_data_analysis.

Covers:
- total_revenue: sums revenue across all Sale records.
- revenue_by_region: groups by region and aggregates revenue.
- revenue_by_category: groups by category and aggregates revenue.
- revenue_by_segment: groups by customer segment and aggregates revenue.
- top_n_products_by_revenue: groups by product, aggregates revenue, and
  sorts to return the top-N products.
"""

import unittest

from src.sales_model import Sale
from src.sales_analysis import (
    total_revenue,
    revenue_by_region,
    revenue_by_category,
    revenue_by_segment,
    top_n_products_by_revenue,
)


class TestSalesAnalysis(unittest.TestCase):
    def setUp(self) -> None:
        # Small, in-memory sample independent of the big CSV
        self.sample_sales = [
            Sale(
                row_id="1",
                order_id="O-1",
                order_date="2024-01-01",
                ship_date="2024-01-03",
                ship_mode="Second Class",
                customer_id="C1",
                customer_name="Alice",
                segment="Consumer",
                country="United States",
                city="New York",
                state="New York",
                postal_code="10001",
                region="East",
                product_id="P1",
                category="Technology",
                sub_category="Phones",
                product_name="Phone A",
                sales=100.0,
                quantity=1,
                discount=0.0,
                profit=20.0,
            ),
            Sale(
                row_id="2",
                order_id="O-2",
                order_date="2024-01-02",
                ship_date="2024-01-04",
                ship_mode="Second Class",
                customer_id="C2",
                customer_name="Bob",
                segment="Corporate",
                country="United States",
                city="Los Angeles",
                state="California",
                postal_code="90001",
                region="West",
                product_id="P2",
                category="Furniture",
                sub_category="Chairs",
                product_name="Chair B",
                sales=200.0,
                quantity=2,
                discount=0.0,
                profit=50.0,
            ),
            Sale(
                row_id="3",
                order_id="O-3",
                order_date="2024-01-03",
                ship_date="2024-01-05",
                ship_mode="Standard Class",
                customer_id="C1",
                customer_name="Alice",
                segment="Consumer",
                country="United States",
                city="New York",
                state="New York",
                postal_code="10001",
                region="East",
                product_id="P1",
                category="Technology",
                sub_category="Phones",
                product_name="Phone A",
                sales=50.0,
                quantity=1,
                discount=0.0,
                profit=10.0,
            ),
        ]

    def test_total_revenue(self):
        self.assertAlmostEqual(total_revenue(self.sample_sales), 350.0)

    def test_revenue_by_region(self):
        result = revenue_by_region(self.sample_sales)
        self.assertAlmostEqual(result["East"], 150.0)
        self.assertAlmostEqual(result["West"], 200.0)

    def test_revenue_by_category(self):
        result = revenue_by_category(self.sample_sales)
        self.assertAlmostEqual(result["Technology"], 150.0)
        self.assertAlmostEqual(result["Furniture"], 200.0)

    def test_revenue_by_segment(self):
        result = revenue_by_segment(self.sample_sales)
        self.assertAlmostEqual(result["Consumer"], 150.0)
        self.assertAlmostEqual(result["Corporate"], 200.0)

    def test_top_n_products_by_revenue(self):
        result = top_n_products_by_revenue(self.sample_sales, 2)
        # totals: Phone A = 150, Chair B = 200
        self.assertEqual(result[0][0], "Chair B")
        self.assertAlmostEqual(result[0][1], 200.0)
        self.assertEqual(result[1][0], "Phone A")
        self.assertAlmostEqual(result[1][1], 150.0)

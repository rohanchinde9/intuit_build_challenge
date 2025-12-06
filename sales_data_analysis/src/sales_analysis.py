# src/sales_analysis.py

from __future__ import annotations

from collections import defaultdict
from typing import Iterable, Dict, List, Tuple

from .sales_model import Sale


def total_revenue(sales: Iterable[Sale]) -> float:
    """Compute total revenue across all sales records."""
    return sum(s.revenue for s in sales)


def revenue_by_region(sales: Iterable[Sale]) -> Dict[str, float]:
    """
    Aggregate total revenue grouped by Region.

    This shows which geographic regions contribute most to overall sales.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.region] += s.revenue
    return dict(totals)


def revenue_by_category(sales: Iterable[Sale]) -> Dict[str, float]:
    """
    Aggregate total revenue grouped by product category.

    Highlights which categories generate the most revenue.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.category] += s.revenue
    return dict(totals)


def revenue_by_segment(sales: Iterable[Sale]) -> Dict[str, float]:
    """
    Aggregate total revenue grouped by customer segment.

    Compares revenue from Consumer, Corporate, and Home Office segments.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.segment] += s.revenue
    return dict(totals)


def top_n_products_by_revenue(
    sales: Iterable[Sale], n: int
) -> List[Tuple[str, float]]:
    """
    Return the top-N products ranked by total revenue.

    Groups by product name, sums revenue per product, then sorts descending.
    """
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.product_name] += s.revenue
    # Functional style: items -> sorted with lambda key
    return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:n]

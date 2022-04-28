from collections import defaultdict
import sys
from typing import List, Optional

import typer


def split(items: List[str], total: int, index: int) -> List[str]:
    round_robin_buckets = defaultdict(list)
    for i, item in enumerate(items):
        round_robin_buckets[i % total].append(item)

    return round_robin_buckets[index]


def validate_items(items: Optional[str]):
    if not items:
        if not sys.stdin.isatty():
            items = sys.stdin.read().strip().split()

    if not items:
        raise typer.BadParameter("items is required")

    return items

def validate_total(total: int) -> int:
    if not total > 0:
        raise typer.BadParameter("total must be greater than zero")
    return total

def validate_index(index: int, total: int):
    if not index < total:
        raise typer.BadParameter("index must be less than total")

def main(
    items: List[str] = typer.Argument(
        None,
        callback=validate_items,
        help="The thing to split up. Typically a list of file names."
    ),
    total: int = typer.Option(1, envvar="PARALLELISM_TOTAL", callback=validate_total),
    index: int = typer.Option(0, envvar="PARALLELISM_INDEX"),
):
    validate_index(index, total)
    target_chunk = split(items, total, index)

    if len(target_chunk) == 0:
        raise typer.BadParameter("Target chunk is empty. Not enough work to distribute. Parallelism values may be too large.")

    typer.echo(" ".join(target_chunk))

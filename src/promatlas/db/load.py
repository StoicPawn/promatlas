"""Loading utilities for the analytical database."""

from typing import Any


def load_dimension_tables(connection: Any) -> None:
    """Load dimension tables into the database."""

    raise NotImplementedError("Dimension loading not yet implemented.")


def load_fact_tables(connection: Any) -> None:
    """Load fact tables into the database."""

    raise NotImplementedError("Fact loading not yet implemented.")

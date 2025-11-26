"""Schema definitions for the analytical database."""

from typing import Any


def create_schema(connection: Any) -> None:
    """Create dimension and fact tables on the provided connection.

    Parameters
    ----------
    connection:
        A database connection object supporting ``execute`` calls.
    """

    raise NotImplementedError("Schema creation not yet implemented.")

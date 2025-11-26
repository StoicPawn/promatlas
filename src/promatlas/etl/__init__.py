"""ETL pipelines for data ingestion."""

from . import bdi_credit, bdap_bilanci, istat_sectors, istat_territory, openbilanci, utils

__all__ = [
    "bdi_credit",
    "istat_sectors",
    "istat_territory",
    "bdap_bilanci",
    "openbilanci",
    "utils",
]

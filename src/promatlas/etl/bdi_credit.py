"""Pipeline to download and parse Banca d'Italia credit data."""

from pathlib import Path


def download(destination: Path) -> None:
    """Download raw credit data into the provided destination folder."""

    raise NotImplementedError("BDI credit download not yet implemented.")


def transform(source: Path, output: Path) -> None:
    """Transform raw credit data into cleaned parquet/csv tables."""

    raise NotImplementedError("BDI credit transform not yet implemented.")

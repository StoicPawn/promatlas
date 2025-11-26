"""Pipeline to download and parse ISTAT sector competitiveness data."""

from pathlib import Path


def download(destination: Path) -> None:
    """Download raw ISTAT sector data into the provided destination folder."""

    raise NotImplementedError("ISTAT sector download not yet implemented.")


def transform(source: Path, output: Path) -> None:
    """Transform raw ISTAT sector data into cleaned tables."""

    raise NotImplementedError("ISTAT sector transform not yet implemented.")

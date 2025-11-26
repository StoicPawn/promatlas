"""Pipeline to download and parse MEF BDAP balance sheet data."""

from pathlib import Path


def download(destination: Path) -> None:
    """Download BDAP balance sheet data into the provided destination folder."""

    raise NotImplementedError("BDAP download not yet implemented.")


def transform(source: Path, output: Path) -> None:
    """Transform BDAP data into cleaned tables."""

    raise NotImplementedError("BDAP transform not yet implemented.")

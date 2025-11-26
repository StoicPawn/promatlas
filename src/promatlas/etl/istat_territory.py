"""Pipeline to download ISTAT demographic/territorial data."""

from pathlib import Path


def download(destination: Path) -> None:
    """Download territorial data into the provided destination folder."""

    raise NotImplementedError("ISTAT territory download not yet implemented.")


def transform(source: Path, output: Path) -> None:
    """Transform raw territorial data into cleaned tables."""

    raise NotImplementedError("ISTAT territory transform not yet implemented.")

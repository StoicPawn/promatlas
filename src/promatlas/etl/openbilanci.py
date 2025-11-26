"""Pipeline to download and parse OpenBilanci data."""

from pathlib import Path


def download(destination: Path) -> None:
    """Download OpenBilanci data into the provided destination folder."""

    raise NotImplementedError("OpenBilanci download not yet implemented.")


def transform(source: Path, output: Path) -> None:
    """Transform OpenBilanci data into cleaned tables."""

    raise NotImplementedError("OpenBilanci transform not yet implemented.")

"""Pipeline to download and parse ISTAT sector competitiveness data."""

from pathlib import Path

from .utils import DownloadItem, download_items


ISTAT_SECTORS_SAMPLE = """ateco2,descrizione,valore_aggiunto_mln,addetti,anno
A,Agricoltura,31800,850000,2021
C,Manifatturiero,275000,3400000,2021
G,Commercio,198000,2900000,2021
"""


def download(destination: Path) -> None:
    """Download raw ISTAT sector data into the provided destination folder."""

    items = [
        DownloadItem(
            url=(
                "https://raw.githubusercontent.com/istat-methods-support/"
                "promatlas-samples/main/istat_settori.csv"
            ),
            filename="istat_settori.csv",
            description="Indicatori competitività settori (CSV ISTAT)",
            fallback_content=ISTAT_SECTORS_SAMPLE,
        )
    ]

    download_items(destination, items)


def transform(source: Path, output: Path) -> None:
    """Transform raw ISTAT sector data into cleaned tables."""

    raise NotImplementedError("ISTAT sector transform not yet implemented.")

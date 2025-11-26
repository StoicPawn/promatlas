"""Pipeline to download and parse MEF BDAP balance sheet data."""

from pathlib import Path

from .utils import DownloadItem, download_items


BDAP_SAMPLE_CSV = """codice_comune,anno,titolo,competenza_accertata,competenza_riscossa
010001,2021,IMPOSTE,1580000,1523000
010001,2021,TRASFERIMENTI,820000,810000
010001,2021,SPESE_CORRENTI,2140000,2085000
"""


def download(destination: Path) -> None:
    """Download BDAP balance sheet data into the provided destination folder."""

    items = [
        DownloadItem(
            url=(
                "https://raw.githubusercontent.com/istat-methods-support/"
                "promatlas-samples/main/bdap_bilanci.csv"
            ),
            filename="bdap_bilanci.csv",
            description="Bilanci enti territoriali (estratto BDAP)",
            fallback_content=BDAP_SAMPLE_CSV,
        )
    ]

    download_items(destination, items)


def transform(source: Path, output: Path) -> None:
    """Transform BDAP data into cleaned tables."""

    raise NotImplementedError("BDAP transform not yet implemented.")

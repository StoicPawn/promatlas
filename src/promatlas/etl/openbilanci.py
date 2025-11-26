"""Pipeline to download and parse OpenBilanci data."""

from pathlib import Path

from .utils import DownloadItem, download_items


OPENBILANCI_SAMPLE_CSV = """codice_comune,anno,voce_importo,competenza
010001,2019,ENTRATE_TRIBUTARIE,1490000
010001,2019,SPESE_TITOLO1,2010000
010001,2020,ENTRATE_TRIBUTARIE,1515000
010001,2020,SPESE_TITOLO1,2060000
"""


def download(destination: Path) -> None:
    """Download OpenBilanci data into the provided destination folder."""

    items = [
        DownloadItem(
            url=(
                "https://raw.githubusercontent.com/istat-methods-support/"
                "promatlas-samples/main/openbilanci.csv"
            ),
            filename="openbilanci.csv",
            description="Serie storiche OpenBilanci",
            fallback_content=OPENBILANCI_SAMPLE_CSV,
        )
    ]

    download_items(destination, items)


def transform(source: Path, output: Path) -> None:
    """Transform OpenBilanci data into cleaned tables."""

    raise NotImplementedError("OpenBilanci transform not yet implemented.")

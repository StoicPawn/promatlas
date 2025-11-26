"""Pipeline to download ISTAT demographic/territorial data."""

from pathlib import Path

from .utils import DownloadItem, download_items


ISTAT_TERRITORY_SAMPLE = """codice_regione,denominazione_regione,popolazione,anno
01,Piemonte,4259500,2022
07,Lazio,5879082,2022
20,Sicilia,4880422,2022
"""


def download(destination: Path) -> None:
    """Download territorial data into the provided destination folder."""

    items = [
        DownloadItem(
            url=(
                "https://raw.githubusercontent.com/istat-methods-support/"
                "promatlas-samples/main/istat_territorio.csv"
            ),
            filename="istat_territorio.csv",
            description="Popolazione e codici ISTAT territoriali",
            fallback_content=ISTAT_TERRITORY_SAMPLE,
        )
    ]

    download_items(destination, items)


def transform(source: Path, output: Path) -> None:
    """Transform raw territorial data into cleaned tables."""

    raise NotImplementedError("ISTAT territory transform not yet implemented.")

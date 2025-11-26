"""Pipeline to download and parse Banca d'Italia credit data."""

from pathlib import Path

from .utils import DownloadItem, download_items


BDI_SAMPLE_CSV = """anno,territorio,settore,impieghi_mln,sofferenze_mln
2022,Italia,Industria,250000,8500
2022,Italia,Servizi,310000,6400
2022,Italia,Costruzioni,120000,5200
"""


def download(destination: Path) -> None:
    """Download raw credit data into the provided destination folder.

    The implementation points to the public CSV export of the Banca d'Italia
    STACORIS dashboard. If the network is unavailable, a lightweight sample
    CSV is written so that the downstream pipeline can still be exercised.
    """

    items = [
        DownloadItem(
            url=(
                "https://raw.githubusercontent.com/istat-methods-support/"
                "promatlas-samples/main/bdi_credit.csv"
            ),
            filename="bdi_credit.csv",
            description="Esportazione STACORIS credit risk",
            fallback_content=BDI_SAMPLE_CSV,
        )
    ]

    download_items(destination, items)


def transform(source: Path, output: Path) -> None:
    """Transform raw credit data into cleaned parquet/csv tables."""

    raise NotImplementedError("BDI credit transform not yet implemented.")

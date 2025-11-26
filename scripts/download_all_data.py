"""Orchestrate download of all open datasets used by PromAtlas."""

from pathlib import Path

from promatlas.config import get_settings
from promatlas import etl


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    settings = get_settings()
    ensure_directory(settings.raw_dir / "bdi")
    ensure_directory(settings.raw_dir / "istat")
    ensure_directory(settings.raw_dir / "bdap")
    ensure_directory(settings.raw_dir / "openbilanci")

    pipelines = {
        "Banca d'Italia": etl.bdi_credit.download,
        "ISTAT settori": etl.istat_sectors.download,
        "ISTAT territorio": etl.istat_territory.download,
        "BDAP": etl.bdap_bilanci.download,
        "OpenBilanci": etl.openbilanci.download,
    }

    for name, func in pipelines.items():
        target = settings.raw_dir / name.lower().replace(" ", "_")
        try:
            func(target)
        except NotImplementedError:
            print(f"[TODO] Download pipeline for {name} non ancora implementata.")


if __name__ == "__main__":
    main()

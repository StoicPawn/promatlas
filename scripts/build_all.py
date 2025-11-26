"""Run full ETL and database build for PromAtlas."""

from pathlib import Path

from promatlas.config import get_settings
from promatlas import etl
from promatlas import db


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    settings = get_settings()
    ensure_directory(settings.interim_dir)
    ensure_directory(settings.processed_dir)

    transforms = {
        "Banca d'Italia": etl.bdi_credit.transform,
        "ISTAT settori": etl.istat_sectors.transform,
        "ISTAT territorio": etl.istat_territory.transform,
        "BDAP": etl.bdap_bilanci.transform,
        "OpenBilanci": etl.openbilanci.transform,
    }

    for name, func in transforms.items():
        source = settings.raw_dir / name.lower().replace(" ", "_")
        output = settings.interim_dir / name.lower().replace(" ", "_")
        ensure_directory(output)
        try:
            func(source, output)
        except NotImplementedError:
            print(f"[TODO] Transform pipeline for {name} non ancora implementata.")

    try:
        connection = settings.database_path  # placeholder
        db.create_schema(connection)
        db.load_dimension_tables(connection)
        db.load_fact_tables(connection)
    except NotImplementedError:
        print("[TODO] Caricamento database non ancora implementato.")


if __name__ == "__main__":
    main()

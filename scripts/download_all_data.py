"""Orchestrate download of all open datasets used by PromAtlas."""

from pathlib import Path
from typing import Callable, Dict

from promatlas.config import get_settings
from promatlas import etl


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


PipelineFunc = Callable[[Path], None]


def run_pipeline(name: str, func: PipelineFunc, base_dir: Path) -> None:
    target = base_dir / name.lower().replace(" ", "_")
    ensure_directory(target)
    print(f"\n>>> {name}")
    try:
        func(target)
    except NotImplementedError:
        print(f"[TODO] Download pipeline per {name} non ancora implementata.")


def main() -> None:
    settings = get_settings()
    ensure_directory(settings.raw_dir)

    pipelines: Dict[str, PipelineFunc] = {
        "Banca d'Italia": etl.bdi_credit.download,
        "ISTAT settori": etl.istat_sectors.download,
        "ISTAT territorio": etl.istat_territory.download,
        "BDAP": etl.bdap_bilanci.download,
        "OpenBilanci": etl.openbilanci.download,
    }

    print("Avvio download di tutte le fonti open...")
    for name, func in pipelines.items():
        run_pipeline(name, func, settings.raw_dir)

    print("\nCompletato. I file sono disponibili in data/raw/.")


if __name__ == "__main__":
    main()

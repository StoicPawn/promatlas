"""Utility helpers for ETL download steps."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import requests


@dataclass(frozen=True)
class DownloadItem:
    """Represent a remote resource to be downloaded."""

    url: str
    filename: str
    description: str
    fallback_content: Optional[str] = None


def stream_download(url: str, destination: Path, timeout: int = 30) -> None:
    """Download a file from ``url`` to ``destination`` using streaming."""

    with requests.get(url, stream=True, timeout=timeout) as response:
        response.raise_for_status()
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("wb") as fp:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    fp.write(chunk)


def download_items(destination: Path, items: Iterable[DownloadItem]) -> None:
    """Download all provided items, skipping files already present.

    If a download fails and a ``fallback_content`` is defined, a lightweight
    placeholder CSV is written instead so downstream steps can still operate
    in offline mode.
    """

    destination.mkdir(parents=True, exist_ok=True)

    for item in items:
        target = destination / item.filename
        if target.exists():
            print(f"[SKIP] {item.description} già presente: {target.name}")
            continue

        try:
            print(f"[DOWNLOAD] {item.description} da {item.url}")
            stream_download(item.url, target)
            print(f"[OK] Salvato {target}")
        except Exception as exc:  # pragma: no cover - network dependent
            if item.fallback_content is None:
                print(f"[ERRORE] Impossibile scaricare {item.description}: {exc}")
                raise

            target.write_text(item.fallback_content, encoding="utf-8")
            print(
                "[OFFLINE] {desc} salvato come campione locale ({err}).".format(
                    desc=item.description, err=exc
                )
            )


__all__ = ["DownloadItem", "download_items", "stream_download"]

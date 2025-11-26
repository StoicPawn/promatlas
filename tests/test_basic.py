"""Smoke tests for initial PromAtlas structure."""


def test_version_import() -> None:
    from promatlas import __version__

    assert __version__ == "0.1.0"

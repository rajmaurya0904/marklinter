"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import marklinter


def test_version_is_set() -> None:
    assert marklinter.__version__

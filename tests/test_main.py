"""Unit tests for the entry point."""

import logging

import pytest

from bulletproof_python import main


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    """Test the entry point."""
    main.main()
    assert caplog.record_tuples == [
        ("root", logging.WARNING, "Hello World"),
    ]

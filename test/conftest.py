import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--dump", action="store_true", default=False,
        help="save output of regression test"
    )

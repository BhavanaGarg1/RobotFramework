# tests/conftest.py
import logging
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        filename="test_log.log",
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logging.info("Starting ETL validation tests...")
    yield
    logging.info("Finished all tests.")

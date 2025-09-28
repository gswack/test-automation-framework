import logging
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        filename='logs/test.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    logging.info("Starting test session")


@pytest.fixture
def sample_data():
    return {"key": "value"}

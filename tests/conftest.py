import pytest

from pyflix import create_app


@pytest.fixture(scope="function")
def app():
    _app = create_app()
    with _app.test_client() as testing_client:
        yield testing_client

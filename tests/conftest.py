import pytest

from pyflix import create_app


@pytest.fixture(scope="function")
def app():
    _app = create_app()
    with _app.test_client() as testing_client:
        with _app.app_context():
            yield testing_client


@pytest.fixture(scope="function")
def keys():
    return {
        "space": "space",
        "skip_forward": "shift+n",
        "volume_up": "up, up, up",
        "volume_down": "down, down, down",
        "toggle_full_screen": "f",
        "skip_10_backward": "left",
        "skip_10_forward": "right",
        "mute": "m",
        "skip_intro": "s",
    }


@pytest.fixture(scope="function")
def pages():
    return ["netflix", "prime", "youtube"]

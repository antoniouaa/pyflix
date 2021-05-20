# pyflix

The project uses [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [keyboard](https://github.com/boppreh/keyboard) to launch a Flask app on your local network for you to issue a few keyboard commands from other devices.

It's intended use is to pause, resume, skip episodes forward and backward and adjust volume when streaming Netflix, Amazon Prime, Disney+, YouTube, etc. They all use similar keyboard shortcuts so it should work across all of them.

## Installation

You're going to need [poetry](https://python-poetry.org/).

```ps
poetry install
```

## Run locally

```ps
$env:FLASK_APP = "wsgi.py"
poetry run flask run -h "0.0.0.0" -p 5000
```

## Testing

```ps
poetry run pytest -vvv
```

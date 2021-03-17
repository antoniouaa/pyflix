from flask import Flask, redirect
from pyflix import routes


def create_app():
    app = Flask(__name__.split(".")[0])
    app.url_map.strict_slashes = False

    register_blueprint(app)

    @app.route("/", methods=["GET"])
    def landing():
        return redirect("/api"), 301

    return app


def register_blueprint(app):
    app.register_blueprint(routes.blueprint, url_prefix="/api")

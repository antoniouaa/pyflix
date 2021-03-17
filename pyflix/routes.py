from flask import Blueprint, render_template
from werkzeug.utils import redirect

blueprint = Blueprint("api_blueprint", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index")


@blueprint.route("/click", methods=["POST"])
def click():
    return redirect("/api"), 301
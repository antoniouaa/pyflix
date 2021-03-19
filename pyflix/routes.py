from flask import Blueprint, render_template, redirect, request, make_response
import keyboard

blueprint = Blueprint("api_blueprint", __name__)

keys = {
    "space": "space",
    "move_next": "shift+n",
    "move_prev": "shift+p",
    "volume_up": "up, up, up",
    "volume_down": "down, down, down",
    "toggle_full_screen": "f",
    "skip_10_backward": "left",
    "skip_10_forward": "right",
    "mute": "m",
    "skip_intro": "s",
    "speed_playback": "shift+>",
    "slow_playback": "shift+<",
}


@blueprint.route("/pages/<page>/click", methods=["POST"])
def click(page):
    try:
        action = next(iter(request.form))
        if action in keys:
            print(f"Performing action: {action}")
        keyboard.send(keys[action])
    except StopIteration:
        print("Form empty")
        action = "error"
    finally:
        return redirect(f"/api/pages/{page}", code=302)


@blueprint.route("/pages/<page>", methods=["GET"])
def commands(page):
    if page is not None:
        return render_template("commands.html", title=page.title(), page=page)
    return redirect("/")


@blueprint.route("/pages", methods=["POST"])
def select_service():
    if "page" in request.form:
        page = request.form["page"]
        return redirect(f"/api/pages/{page}")
    return render_template("index.html", title="pyflix")


@blueprint.route("/pages", methods=["GET"])
@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="pyflix")

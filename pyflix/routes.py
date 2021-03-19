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

current_page = ""


@blueprint.route("/pages", methods=["POST"])
def page_post():
    global current_page
    if "page" in request.form:
        current_page = request.form["page"]
    return render_template(
        "commands.html", title=current_page.title(), page=current_page
    )


@blueprint.route("/click", methods=["POST"])
def click():
    try:
        action = next(iter(request.form))
        if action in keys:
            print(f"Performing action: {action}")
        keyboard.send(keys[action])
    except StopIteration:
        print("Form empty")
        action = "error"
    finally:
        response = make_response(redirect("/api/pages", code=307))
        response.headers["Option-Clicked"] = action
        return response


@blueprint.route("/", methods=["GET"])
def index():
    global current_page
    current_page = ""
    return render_template("index.html", title="pyflix")

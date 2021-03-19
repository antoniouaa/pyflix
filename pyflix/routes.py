from flask import Blueprint, render_template, redirect, request, make_response
import keyboard

blueprint = Blueprint("api_blueprint", __name__)

keys = {
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


@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index")


@blueprint.route("/click", methods=["POST"])
def click():
    try:
        action = next(iter(request.form))
        if action in keys:
            print(f"Performing action: {keys[action]}")
        keyboard.send(keys[action])
    except StopIteration:
        print("Form empty")
        action = "error"
    finally:
        response = make_response(redirect("/api"))
        response.headers["Option-Clicked"] = action
        return response

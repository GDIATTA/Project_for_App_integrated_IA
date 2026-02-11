from flask import Blueprint, render_template

items_bp = Blueprint("items", __name__)

@items_bp.route("/")
def home():
    return render_template("home.html")
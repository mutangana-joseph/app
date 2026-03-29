from flask import Blueprint, request, jsonify, render_template
import time

counter = Blueprint("counter", __name__, url_prefix="/counter")


@counter.route("/")
def show_result():
    return render_template("counter.html")

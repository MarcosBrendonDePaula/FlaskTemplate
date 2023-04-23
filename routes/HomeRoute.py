from flask import Blueprint, request, render_template
route_home = Blueprint('home', __name__)


@route_home.route("/")
def hello_world():
    return render_template("teste.html")
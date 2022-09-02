from flask import Blueprint
from flask import redirect
from application import app
from flask import render_template
route_index = Blueprint('index_page', __name__)


@route_index.route("/index")
def index():
    # return "ok!"
    # return redirect('http://www.baidu.com')
    return render_template("index.html")
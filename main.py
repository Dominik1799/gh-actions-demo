from flask import Flask
from flask import render_template
from logic import get_today

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", date=get_today())



app.run()
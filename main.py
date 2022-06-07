from flask import Flask
from flask import render_template
from logic import get_today

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def hello_world():
    return render_template("index.html", date=get_today())



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)

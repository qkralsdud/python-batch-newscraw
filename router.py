from flask import Flask
from flask.templating import render_template
import newsapp_api as nsa

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", newsList=nsa.getNewsApiProj())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
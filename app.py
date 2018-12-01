from flask import Flask, render_template
import json
from generatetweet import make_tweet

app = Flask(__name__)


@app.route("/gettweet", methods=["GET"])
def get_tweet():
    return json.dumps(make_tweet())

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/game/<numq>/<time>")
def game(numq=0, time=0):
    try:
        numq = int(numq)
        time = int(time)
    except BaseException:
        return "no"

    if numq < 5 or numq > 25:
        pass
        #return "no"

    if time < 5 or time > 30:
        pass
        #return "no"

    return render_template("game.html", numq=numq, time=time)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")
   # add start button with link to "\game"

@app.route("/game")
def play():
    return render_template("game.html")


if __name__ == "__main__":

   app.run(host='0.0.0.0', port=3000)


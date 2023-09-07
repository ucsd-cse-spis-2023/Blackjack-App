from flask import Flask, render_template
# import deap

# deap.do_stuff()
# deap_model = woohoo!

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")

@app.route("/game")
def play():
    return render_template("game.html")


if __name__ == "__main__":

   app.run(host='0.0.0.0', port=5002)


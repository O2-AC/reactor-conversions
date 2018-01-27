from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/variables", methods=["POST"])
def variables():
    if not request.form.get("rateConstant") or not request.form.get("tauCSTR") or not request.form.get("tauPFR") or not request.form.get("reactionOrder"):
        return render_template("error.html")
    k = request.form.get("rateConstant")
    tCSTR = request.form.get("tauCSTR")
    tPFR = request.form.get("tauPFR")
    if request.form.get("reactionOrder") == "firstOrder":
        return render_template("results.html")
    elif request.form.get("reactionOrder") == "secondOrder":
        return render_template("results.html")

if __name__ == "__main__":
    app.run()

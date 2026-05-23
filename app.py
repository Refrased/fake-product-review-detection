from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        review = request.form["review"]

        result = model.predict([review])[0]

        if result == 1:
            prediction = "Genuine Review"
        else:
            prediction = "Fake Review"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import numpy as np
import pickle

# Load models

crop_model = pickle.load(
    open("crop_model.pkl", "rb")
)

fertilizer_model = pickle.load(
    open("fertilizer_model.pkl", "rb")
)

yield_model = pickle.load(
    open("yield_model.pkl", "rb")
)

# Load accuracy

with open("accuracy.txt", "r") as file:
    accuracy = file.read()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    crop_prediction = None
    fertilizer_prediction = None
    yield_prediction = None

    if request.method == "POST":

        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])

        temperature = float(
            request.form["temperature"]
        )

        humidity = float(
            request.form["humidity"]
        )

        ph = float(request.form["ph"])

        rainfall = float(
            request.form["rainfall"]
        )

        # Crop Prediction

        crop_data = np.array([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        crop_prediction = crop_model.predict(
            crop_data
        )[0]

        # Fertilizer Prediction

        fertilizer_data = np.array([[
            N,
            P,
            K,
            1
        ]])

        fertilizer_prediction = (
            fertilizer_model.predict(
                fertilizer_data
            )[0]
        )

        # Yield Prediction

        yield_data = np.array([[
            rainfall,
            temperature,
            humidity
        ]])

        yield_prediction = (
            yield_model.predict(
                yield_data
            )[0]
        )

    return render_template(
        "index.html",
        crop_prediction=crop_prediction,
        fertilizer_prediction=fertilizer_prediction,
        yield_prediction=yield_prediction,
        accuracy=accuracy
    )

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 5000
            )
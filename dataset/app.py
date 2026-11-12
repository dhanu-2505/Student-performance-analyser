
from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model_path = os.path.join("models", "student_model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    attendance = float(request.form["attendance"])
    study_hours = float(request.form["study_hours"])
    previous_marks = float(request.form["previous_marks"])
    internal_marks = float(request.form["internal_marks"])

    input_data = [[
        attendance,
        study_hours,
        previous_marks,
        internal_marks
    ]]

    prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

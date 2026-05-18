from flask import Flask, request, jsonify
import joblib
import numpy as np
import os 
from dotenv import load_dotenv 
load_dotenv()
app = Flask(__name__)
MODEL_PATH = os.getenv("MODEL_PATH")

model = joblib.load(open(MODEL_PATH, "rb"))

label_map = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obesity",
    5: "Extreme Obesity"
}


@app.route('/')
def home():
    return "<h3>This is my home page</h3>"


@app.route('/about')
def about():
    return "<h3>This is About Page</h3><br>The program is a structured and exhaustive engagement for the eligible students with a strong focus on helping them develop the relevant Artificial Intelligence skills through an experiential learning methodology. The program is delivered over 12 months."

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form['gender']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    
    gender_encoded = 1 if gender == "Male" else 0

    input_data = np.array([[gender_encoded, height, weight]])
    prediction = model.predict(input_data)[0]
    
    return jsonify({
    "prediction": label_map[prediction]
    })



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from flasgger import Swagger
from tensorflow.keras.models import load_model
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
swagger = Swagger(app)  # Initialize Swagger UI

# Set paths properly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'model', 'mood_predictor.keras')
SCALER_PATH = os.path.join(BASE_DIR, '..', 'model', 'scaler.pkl')

# Load model and scaler
model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@app.route('/')
def home():
    return "✅ MindEase ML Engine is running properly! 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict Mood Level 🎯
    ---
    post:
      description: Predict the mood score based on user activity data.
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          schema:
            type: object
            properties:
              sleep_hours:
                type: number
                example: 7
              screen_time:
                type: number
                example: 5
              physical_activity:
                type: number
                example: 30
              journal_freq:
                type: integer
                example: 2
              previous_mood:
                type: number
                example: 6
            required:
              - sleep_hours
              - screen_time
              - physical_activity
              - journal_freq
              - previous_mood
      responses:
        200:
          description: Successfully returns mood score prediction
          content:
            application/json:
              schema:
                type: object
                properties:
                  predicted_mood:
                    type: number
    """
    try:
        data = request.get_json()

        required_fields = ["sleep_hours", "screen_time", "physical_activity", "journal_freq", "previous_mood"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        features = [
            data['sleep_hours'],
            data['screen_time'],
            data['physical_activity'],
            data['journal_freq'],
            data['previous_mood']
        ]

        features_scaled = scaler.transform([features])

        prediction = model.predict(features_scaled)[0][0]

        return jsonify({
            "predicted_mood": float(round(prediction, 2))  # 🚀 Fixed float32 bug here
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
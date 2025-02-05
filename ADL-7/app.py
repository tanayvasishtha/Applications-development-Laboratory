from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

def load_model():
    try:
        if not os.path.exists('house_data.pkl'):
            raise FileNotFoundError("Model file not found. Please run model.py first.")
        
        with open('house_data.pkl', 'rb') as file:
            model, scaler, features = pickle.load(file)
            return model, scaler, features
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None, None

model, scaler, features = load_model()

@app.route('/')
def home():
    if model is None:
        return "Error: Model not loaded. Please train the model first.", 500
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None or scaler is None:
            return "Error: Model not loaded. Please train the model first.", 500

        # Get values from the form
        input_features = []
        for feature in features:
            value = float(request.form[feature])
            input_features.append(value)

        # Convert to numpy array and reshape
        input_features = np.array(input_features).reshape(1, -1)
        
        # Scale the features
        features_scaled = scaler.transform(input_features)

        # Make prediction
        prediction = model.predict(features_scaled)
        output = round(prediction[0], 2)

        return render_template('index.html', 
                             prediction_text=f'Predicted House Price: ${output:,}')

    except Exception as e:
        return f"Error during prediction: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)

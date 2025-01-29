import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Path to the pickle file
PICKLE_FILE = os.path.join("models", "calculator.pkl")

def load_data():
    """
    Load computation history from the pickle file.
    If the file doesn't exist or is empty, return an empty list.
    """
    try:
        # Check if the file exists and is not empty
        if not os.path.exists(PICKLE_FILE) or os.path.getsize(PICKLE_FILE) == 0:
            return []  # Return an empty list if no valid data exists
        with open(PICKLE_FILE, "rb") as f:
            return pickle.load(f)
    except (EOFError, pickle.UnpicklingError):
        print("Pickle file is corrupted or unreadable. Returning an empty history.")
        return []

def save_data(data):
    """
    Save computation history to the pickle file.
    """
    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(data, f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    history = load_data()
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        try:
            val1 = float(num1)
            val2 = float(num2)
            result = val1 + val2
            # Store the new result in history
            history.append(f"{val1} + {val2} = {result}")
            save_data(history)
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    # Ensure the models directory exists
    os.makedirs("models", exist_ok=True)
    
    # Initialize the pickle file if it doesn't exist
    if not os.path.exists(PICKLE_FILE):
        save_data([])  # Create an empty list in the pickle file
    
    app.run(debug=True)

from flask import Flask, render_template, request
from models.model import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        try:
            result = calculator.add_numbers(num1, num2)
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template("index.html", result=result, history=calculator.history)

if __name__ == "__main__":
    app.run(debug=True)

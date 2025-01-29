import os
import pickle

class Calculator:
    def __init__(self, pickle_file='models/calculator.pkl'):
        self.pickle_file = pickle_file
        self.history = self.load_history()
    
    def load_history(self):
        """Load computation history from pickle file"""
        try:
            if os.path.exists(self.pickle_file):
                with open(self.pickle_file, 'rb') as f:
                    return pickle.load(f)
            return []
        except (EOFError, pickle.UnpicklingError):
            return []
    
    def save_history(self):
        """Save computation history to pickle file"""
        os.makedirs(os.path.dirname(self.pickle_file), exist_ok=True)
        with open(self.pickle_file, 'wb') as f:
            pickle.dump(self.history, f)
    
    def add_numbers(self, num1, num2):
        """Add two numbers and save to history"""
        result = float(num1) + float(num2)
        computation = f"{num1} + {num2} = {result}"
        self.history.append(computation)
        self.save_history()
        return result

# Initialize the calculator and create pickle file
if __name__ == "__main__":
    calculator = Calculator()
    calculator.save_history()
    print("Calculator pickle file initialized successfully!")

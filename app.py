# ===================================================
# Calculator with History - Flask Web Application
# Author: Indra Chand
# Description: A web-based calculator using Python Flask
# ===================================================

from flask import Flask, render_template, request, jsonify

# Create Flask application
app = Flask(__name__)

# List to store calculation history
calculation_history = []


# ============ CALCULATOR FUNCTIONS ============

def add(num1, num2):
    """Add two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract second number from first."""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Divide first number by second."""
    if num2 == 0:
        return None  # Cannot divide by zero
    return num1 / num2


def calculate(expression):
    """
    Calculate the result of a mathematical expression.
    Returns the result or an error message.
    """
    try:
        # Replace percentage with division by 100
        expression = expression.replace('%', '/100')
        
        # Safely evaluate the expression
        result = eval(expression)
        
        # Round if float
        if isinstance(result, float):
            result = round(result, 8)
        
        return {"success": True, "result": result}
    
    except ZeroDivisionError:
        return {"success": False, "error": "Cannot divide by zero!"}
    
    except Exception as e:
        return {"success": False, "error": "Invalid expression!"}


# ============ FLASK ROUTES ============

@app.route("/")
def home():
    """Display the calculator page."""
    return render_template("index.html", history=calculation_history)


@app.route("/calculate", methods=["POST"])
def calculate_route():
    """API endpoint to perform calculation."""
    # Get expression from request
    data = request.get_json()
    expression = data.get("expression", "")
    
    # Calculate result
    result = calculate(expression)
    
    # Save to history if successful
    if result["success"]:
        history_record = f"{expression} = {result['result']}"
        calculation_history.append(history_record)
        result["history"] = calculation_history
    
    return jsonify(result)


@app.route("/history", methods=["GET"])
def get_history():
    """API endpoint to get calculation history."""
    return jsonify({"history": calculation_history})


@app.route("/clear-history", methods=["POST"])
def clear_history():
    """API endpoint to clear history."""
    global calculation_history
    calculation_history = []
    return jsonify({"success": True, "message": "History cleared!"})


# Run the application
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("   Calculator Web App is running!")
    print("   Open your browser and go to:")
    print("   http://127.0.0.1:5000")
    print("=" * 50 + "\n")
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

app = Flask(__name__)

Talisman(app, force_https=False)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

history = list()

def sanitize_input(value):
    if isinstance(value, (int,float)):
        return value
    try:
        return float(value)
    except(ValueError, TypeError):
        return None

def validate_data():
    data = request.get_json(silent=True)
    if data is None:
        return None, None, ("Invalid or missing JSON", 400)
    
    if 'a' not in data or 'b' not in data:
        return None, None, ("Missing required fields 'a' and 'b'", 400)

    a = sanitize_input(data["a"])
    b = sanitize_input(data["b"])

    if a is None or b is None:
        return None, None, ("Invalid data types. Numbers required", 400)
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None, None, ("Invalid data types. Numbers required", 400)
    
    if abs(a) > 1e15 or abs(b) > 1e15:
        return None, None, ("Numbers too large", 400)
        
    return a, b, None

@app.route("/")
def home():
    return jsonify({'message': 'Welcome to the Flask App!'})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
@limiter.limit("100 per second")
def add():
    a, b, error = validate_data()

    if error:
        return jsonify({"error": error[0]}), error[1]

    result = a + b
    history.append({"a": a, "b": b, "result": result, "operation": "add"})
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
@limiter.limit("100 per second")
def subtract():
    a, b, error = validate_data()
    if error:
        return jsonify({"error": error[0]}), error[1]
        
    result = a - b
    history.append({"a": a, "b": b, "result": result, "operation": "subtract"})
    return jsonify({"result": result})

@app.route("/multiply", methods=["POST"])
@limiter.limit("100 per second")
def multiply():
    a, b, error = validate_data()
    if error:
        return jsonify({"error": error[0]}), error[1]
        
    result = a * b
    history.append({"a": a, "b": b, "result": result, "operation": "multiply"})
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
@limiter.limit("100 per second)
def divide():
    a, b, error = validate_data()
    if error:
        return jsonify({"error": error[0]}), error[1]
    
    if b == 0:
        return jsonify({"error": "Division by zero is not permitted"}), 400

    result = a / b
    history.append({"a": a, "b": b, "result": result, "operation": "divide"})
    return jsonify({"result": result})

@app.route("/history")
@limiter.limit("5 per second")
def show_history():
    return jsonify(history)


if __name__ == "__main__":
    app.run(debug=True)

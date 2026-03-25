from flask import Flask, jsonify, request

app = Flask(__name__)

history = list()

@app.route("/")
def home():
    return jsonify({'message': 'Welcome to the Flask App!'})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data["a"]
    b = data["b"]
    result = a + b
    history.append({"a": a, "b": b, "result": result, "operation": "add"})
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a = data["a"]
    b = data["b"]
    result = a - b
    history.append({"a": a, "b": b, "result": result, "operation": "subtract"})
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data["a"]
    b = data["b"]
    result = a * b
    history.append({"a": a, "b": b, "result": result, "operation": "multiply"})
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data["a"]
    b = data["b"]
    if b == 0:
        return jsonify({"error": "Bad request"}), 400
    result = a / b
    history.append({"a": a, "b": b, "result": result, "operation": "divide"})
    return jsonify({"result": result})

@app.route("/history")
def show_history():
    return jsonify(history)


if __name__ == "__main__":
    app.run(debug=True)

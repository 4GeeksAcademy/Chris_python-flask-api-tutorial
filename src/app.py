from flask import Flask, request, jsonify

app = Flask(__name__)

# Declare the global variable todos
todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.json
    if "label" not in new_todo or "done" not in new_todo:
        return jsonify({"error": "Invalid todo format"}), 400
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)
app = Flask(__name__)

# Declare the global variable todos
todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.json
    if "label" not in new_todo or "done" not in new_todo:
        return jsonify({"error": "Invalid todo format"}), 400
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)
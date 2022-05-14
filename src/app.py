from flask import Flask, jsonify, request


app = Flask(__name__)



@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    
    return json_text

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]


@app.route('/todos', methods=['POST'])
def add_new_todo():
    payload = request.get_json(force=True)
    todos.append(payload)
    return jsonify(todos)
    
    # print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
    # print("This is the position to delete: ",position)
    # return 'something'



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
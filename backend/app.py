from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

@app.route('/reviews/<string:product>/<string:aspect>/<string:sentiment>', methods=['GET'])
def get_reviews(product,aspect,sentiment):
    with open(os.path.abspath(f"./backend/datasets/speakers/{product.lower()}/{aspect.lower()}/{sentiment.lower()}.json"),'r') as f:
        json_string = f.read()

        return json_string



# Run the application
if __name__ == '__main__':
    app.run(debug=True)

'''
# Define some sample data
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# Define routes for each CRUD operation

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Read all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Read a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Update a specific task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400)
    if 'description' in request.json and not isinstance(request.json['description'], str):
        abort(400)
    if 'done' in request.json and not isinstance(request.json['done'], bool):
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# Delete a specific task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
'''

'''
For API end point testing:
URL = "http://127.0.0.1:5000/"
products = ["bose","jbl","sony"]
aspects = ["bass","build","price"]
sentiments = ["bad","good"]

for product in products:
    for aspect in aspects:
        for sentiment in sentiments:
            print(f"{URL}reviews/{product.lower()}/{aspect.lower()}/{sentiment.lower()}")
---------------
http://127.0.0.1:5000/reviews/bose/bass/bad
http://127.0.0.1:5000/reviews/bose/bass/good
http://127.0.0.1:5000/reviews/bose/build/bad
http://127.0.0.1:5000/reviews/bose/build/good
http://127.0.0.1:5000/reviews/bose/price/bad
http://127.0.0.1:5000/reviews/bose/price/good
http://127.0.0.1:5000/reviews/jbl/bass/bad
http://127.0.0.1:5000/reviews/jbl/bass/good
http://127.0.0.1:5000/reviews/jbl/build/bad
http://127.0.0.1:5000/reviews/jbl/build/good
http://127.0.0.1:5000/reviews/jbl/price/bad
http://127.0.0.1:5000/reviews/jbl/price/good
http://127.0.0.1:5000/reviews/sony/bass/bad
http://127.0.0.1:5000/reviews/sony/bass/good
http://127.0.0.1:5000/reviews/sony/build/bad
http://127.0.0.1:5000/reviews/sony/build/good
http://127.0.0.1:5000/reviews/sony/price/bad
http://127.0.0.1:5000/reviews/sony/price/good
'''
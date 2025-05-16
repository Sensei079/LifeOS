from flask import Blueprint, request, jsonify
import uuid

tasks_bp = Blueprint('tasks', __name__)

tasks = {}


@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values()))


@tasks_bp.route('/', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = str(uuid.uuid4())
    task = {
        'id': task_id,
        'title': data.get('title'),
        'due_date': data.get('due_date'),
        'priority': data.get('priority', 'Medium'),
        'status': data.get('status', 'Pending')
    }
    tasks[task_id] = task
    return jsonify(task), 201


@tasks_bp.route('/<task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    tasks[task_id].update(data)
    return jsonify(tasks[task_id])


@tasks_bp.route('/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    del tasks[task_id]
    return jsonify({'message': 'Deleted'})

from flask import Blueprint, request, jsonify
import uuid

health_bp = Blueprint('health', __name__)

health_logs = {}


@health_bp.route('/', methods=['GET'])
def get_health_logs():
    return jsonify(list(health_logs.values()))


@health_bp.route('/', methods=['POST'])
def add_health_log():
    data = request.get_json()
    log_id = str(uuid.uuid4())
    log = {
        'id': log_id,
        'date': data.get('date'),
        'mood': data.get('mood'),
        'steps': data.get('steps'),
        'sleep_hours': data.get('sleep_hours'),
        'water_intake_liters': data.get('water_intake_liters')
    }
    health_logs[log_id] = log
    return jsonify(log), 201


@health_bp.route('/<log_id>', methods=['PUT'])
def update_health_log(log_id):
    if log_id not in health_logs:
        return jsonify({'error': 'Health log not found'}), 404
    data = request.get_json()
    health_logs[log_id].update(data)
    return jsonify(health_logs[log_id])


@health_bp.route('/<log_id>', methods=['DELETE'])
def delete_health_log(log_id):
    if log_id not in health_logs:
        return jsonify({'error': 'Health log not found'}), 404
    del health_logs[log_id]
    return jsonify({'message': 'Deleted'})

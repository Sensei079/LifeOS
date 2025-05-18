from flask import Blueprint, request, jsonify
import uuid

calendar_bp = Blueprint('calendar', __name__)

events = {}


@calendar_bp.route('/', methods=['GET'])
def get_events():
    return jsonify(list(events.values()))


@calendar_bp.route('/', methods=['POST'])
def add_event():
    data = request.get_json()
    event_id = str(uuid.uuid4())
    event = {
        'id': event_id,
        'title': data.get('title'),
        'date': data.get('date'),
        'time': data.get('time'),
        'description': data.get('description', '')
    }
    events[event_id] = event
    return jsonify(event), 201


@calendar_bp.route('/<event_id>', methods=['PUT'])
def update_event(event_id):
    if event_id not in events:
        return jsonify({'error': 'Event not found'}), 404
    data = request.get_json()
    events[event_id].update(data)
    return jsonify(events[event_id])


@calendar_bp.route('/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    if event_id not in events:
        return jsonify({'error': 'Event not found'}), 404
    del events[event_id]
    return jsonify({'message': 'Deleted'})

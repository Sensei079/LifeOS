from flask import Blueprint, request, jsonify
import uuid

notes_bp = Blueprint('notes', __name__)

notes = {}


@notes_bp.route('/', methods=['GET'])
def get_notes():
    return jsonify(list(notes.values()))


@notes_bp.route('/', methods=['POST'])
def add_note():
    data = request.get_json()
    note_id = str(uuid.uuid4())
    note = {
        'id': note_id,
        'title': data.get('title'),
        'content': data.get('content'),
        'tags': data.get('tags', [])
    }
    notes[note_id] = note
    return jsonify(note), 201


@notes_bp.route('/<note_id>', methods=['PUT'])
def update_note(note_id):
    if note_id not in notes:
        return jsonify({'error': 'Note not found'}), 404
    data = request.get_json()
    notes[note_id].update(data)
    return jsonify(notes[note_id])


@notes_bp.route('/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    if note_id not in notes:
        return jsonify({'error': 'Note not found'}), 404
    del notes[note_id]
    return jsonify({'message': 'Deleted'})

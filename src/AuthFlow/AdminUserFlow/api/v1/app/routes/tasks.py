from flask import Blueprint, jsonify, request
from models import db, Task
import traceback

tasks_bp = Blueprint('tasks', __name__)

# GET all tasks
@tasks_bp.route('', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        task_list = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in tasks]
        return jsonify({'tasks': task_list})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# GET a specific task by ID
@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# CREATE a new task
@tasks_bp.route('', methods=['POST'])
def create_task():
    try:
        data = request.json
        title = data.get('title')
        completed = data.get('completed', False)
        new_task = Task(title=title, completed=completed)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully'}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# UPDATE an existing task by ID
@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        data = request.json
        title = data.get('title')
        completed = data.get('completed')

        task.title = title
        task.completed = completed
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# DELETE a task by ID
@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

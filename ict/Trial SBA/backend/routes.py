from flask import request, jsonify
from db import query_one, query_all, execute

def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

def register_routes(app):

    # ============== STUDENT ROUTES ==============

    @app.route('/api/students', methods=['GET'])
    def get_students():
        rows = query_all("SELECT * FROM student")
        return jsonify(rows)

    @app.route('/api/students', methods=['POST'])
    def create_student():
        data = request.get_json()
        if not data or not all(k in data for k in ('gender', 'name', 'form')):
            return error_response('Missing required fields: gender, name, form')
        sid = execute(
            "INSERT INTO student (gender, name, form) VALUES (%s, %s, %s)",
            (data['gender'], data['name'], data['form'])
        )
        row = query_one("SELECT * FROM student WHERE student_id = %s", (sid,))
        return jsonify(row), 201

    @app.route('/api/students/<int:id>', methods=['GET'])
    def get_student(id):
        row = query_one("SELECT * FROM student WHERE student_id = %s", (id,))
        if not row:
            return error_response('Student not found', 404)
        return jsonify(row)

    @app.route('/api/students/<int:id>', methods=['PUT'])
    def update_student(id):
        data = request.get_json()
        execute(
            "UPDATE student SET gender=%s, name=%s, form=%s WHERE student_id=%s",
            (data.get('gender'), data.get('name'), data.get('form'), id)
        )
        row = query_one("SELECT * FROM student WHERE student_id = %s", (id,))
        if not row:
            return error_response('Student not found', 404)
        return jsonify(row)

    @app.route('/api/students/<int:id>', methods=['DELETE'])
    def delete_student(id):
        execute("DELETE FROM student WHERE student_id = %s", (id,))
        return jsonify({'message': 'Student deleted'})

    # ============== CATEGORY ROUTES ==============

    @app.route('/api/categories', methods=['GET'])
    def get_categories():
        rows = query_all("SELECT * FROM category")
        return jsonify(rows)

    @app.route('/api/categories', methods=['POST'])
    def create_category():
        data = request.get_json()
        if not data or not all(k in data for k in ('student_id', 'name')):
            return error_response('Missing required fields: student_id, name')
        cid = execute(
            "INSERT INTO category (student_id, name) VALUES (%s, %s)",
            (data['student_id'], data['name'])
        )
        row = query_one("SELECT * FROM category WHERE category_id = %s", (cid,))
        return jsonify(row), 201

    @app.route('/api/categories/<int:id>', methods=['GET'])
    def get_category(id):
        row = query_one("SELECT * FROM category WHERE category_id = %s", (id,))
        if not row:
            return error_response('Category not found', 404)
        return jsonify(row)

    @app.route('/api/categories/<int:id>', methods=['PUT'])
    def update_category(id):
        data = request.get_json()
        execute(
            "UPDATE category SET name=%s WHERE category_id=%s",
            (data.get('name'), id)
        )
        row = query_one("SELECT * FROM category WHERE category_id = %s", (id,))
        if not row:
            return error_response('Category not found', 404)
        return jsonify(row)

    @app.route('/api/categories/<int:id>', methods=['DELETE'])
    def delete_category(id):
        execute("DELETE FROM category WHERE category_id = %s", (id,))
        return jsonify({'message': 'Category deleted'})

    # ============== WORKSPACE ROUTES ==============

    @app.route('/api/workspaces', methods=['GET'])
    def get_workspaces():
        rows = query_all("SELECT * FROM workspace")
        return jsonify(rows)

    @app.route('/api/workspaces', methods=['POST'])
    def create_workspace():
        data = request.get_json()
        if not data or not all(k in data for k in ('student_id', 'name')):
            return error_response('Missing required fields: student_id, name')
        wid = execute(
            "INSERT INTO workspace (student_id, name) VALUES (%s, %s)",
            (data['student_id'], data['name'])
        )
        row = query_one("SELECT * FROM workspace WHERE workspace_id = %s", (wid,))
        return jsonify(row), 201

    @app.route('/api/workspaces/<int:id>', methods=['GET'])
    def get_workspace(id):
        row = query_one("SELECT * FROM workspace WHERE workspace_id = %s", (id,))
        if not row:
            return error_response('Workspace not found', 404)
        return jsonify(row)

    @app.route('/api/workspaces/<int:id>', methods=['PUT'])
    def update_workspace(id):
        data = request.get_json()
        execute(
            "UPDATE workspace SET name=%s WHERE workspace_id=%s",
            (data.get('name'), id)
        )
        row = query_one("SELECT * FROM workspace WHERE workspace_id = %s", (id,))
        if not row:
            return error_response('Workspace not found', 404)
        return jsonify(row)

    @app.route('/api/workspaces/<int:id>', methods=['DELETE'])
    def delete_workspace(id):
        execute("DELETE FROM workspace WHERE workspace_id = %s", (id,))
        return jsonify({'message': 'Workspace deleted'})

    # ============== TASK ROUTES ==============

    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        rows = query_all("SELECT * FROM task")
        return jsonify(rows)

    @app.route('/api/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        if not data or 'name' not in data or 'student_id' not in data:
            return error_response('Missing required fields: name, student_id')
        due_date = data.get('due_date')
        tid = execute(
            "INSERT INTO task (student_id, category_id, workspace_id, name, description, priority, completion, due_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                data['student_id'],
                data.get('category_id'),
                data.get('workspace_id'),
                data['name'],
                data.get('description'),
                data.get('priority', 'Medium'),
                data.get('completion', False),
                due_date
            )
        )
        row = query_one("SELECT * FROM task WHERE task_id = %s", (tid,))
        return jsonify(row), 201

    @app.route('/api/tasks/<int:id>', methods=['GET'])
    def get_task(id):
        row = query_one("SELECT * FROM task WHERE task_id = %s", (id,))
        if not row:
            return error_response('Task not found', 404)
        return jsonify(row)

    @app.route('/api/tasks/<int:id>', methods=['PUT'])
    def update_task(id):
        data = request.get_json()
        due_date = data.get('due_date')
        execute(
            "UPDATE task SET name=%s, description=%s, priority=%s, completion=%s, category_id=%s, workspace_id=%s, due_date=%s WHERE task_id=%s",
            (
                data.get('name'),
                data.get('description'),
                data.get('priority'),
                data.get('completion'),
                data.get('category_id'),
                data.get('workspace_id'),
                due_date,
                id
            )
        )
        row = query_one("SELECT * FROM task WHERE task_id = %s", (id,))
        if not row:
            return error_response('Task not found', 404)
        return jsonify(row)

    @app.route('/api/tasks/<int:id>', methods=['DELETE'])
    def delete_task(id):
        execute("DELETE FROM task WHERE task_id = %s", (id,))
        return jsonify({'message': 'Task deleted'})

    # ============== REMINDER ROUTES ==============

    @app.route('/api/reminders', methods=['GET'])
    def get_reminders():
        rows = query_all("SELECT * FROM reminder")
        return jsonify(rows)

    @app.route('/api/reminders', methods=['POST'])
    def create_reminder():
        data = request.get_json()
        if not data or not all(k in data for k in ('task_id', 'reminder_time')):
            return error_response('Missing required fields: task_id, reminder_time')
        rid = execute(
            "INSERT INTO reminder (task_id, reminder_time, message) VALUES (%s, %s, %s)",
            (data['task_id'], data['reminder_time'], data.get('message'))
        )
        row = query_one("SELECT * FROM reminder WHERE reminder_id = %s", (rid,))
        return jsonify(row), 201

    @app.route('/api/reminders/<int:id>', methods=['GET'])
    def get_reminder(id):
        row = query_one("SELECT * FROM reminder WHERE reminder_id = %s", (id,))
        if not row:
            return error_response('Reminder not found', 404)
        return jsonify(row)

    @app.route('/api/reminders/<int:id>', methods=['PUT'])
    def update_reminder(id):
        data = request.get_json()
        execute(
            "UPDATE reminder SET reminder_time=%s, message=%s WHERE reminder_id=%s",
            (data.get('reminder_time'), data.get('message'), id)
        )
        row = query_one("SELECT * FROM reminder WHERE reminder_id = %s", (id,))
        if not row:
            return error_response('Reminder not found', 404)
        return jsonify(row)

    @app.route('/api/reminders/<int:id>', methods=['DELETE'])
    def delete_reminder(id):
        execute("DELETE FROM reminder WHERE reminder_id = %s", (id,))
        return jsonify({'message': 'Reminder deleted'})

    # ============== HEALTH CHECK ==============

    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({'status': 'ok'})

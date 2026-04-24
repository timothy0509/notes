# Flask Todo Backend

A simple Flask backend for the todo list application based on the provided ER Diagram. Uses raw PyMySQL (no ORM).

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the MySQL database and tables (run once):
```bash
python init_db.py
```

3. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Database Configuration

- **Engine:** MySQL (via PyMySQL)
- **Host:** localhost
- **Port:** 3307
- **Database:** todo_db
- **User:** root
- **Password:** usbw

## API Endpoints

### Students
- `GET /api/students` - List all students
- `POST /api/students` - Create a new student
- `GET /api/students/<id>` - Get a specific student
- `PUT /api/students/<id>` - Update a student
- `DELETE /api/students/<id>` - Delete a student

### Categories
- `GET /api/categories` - List all categories
- `POST /api/categories` - Create a new category
- `GET /api/categories/<id>` - Get a specific category
- `PUT /api/categories/<id>` - Update a category
- `DELETE /api/categories/<id>` - Delete a category

### Workspaces
- `GET /api/workspaces` - List all workspaces
- `POST /api/workspaces` - Create a new workspace
- `GET /api/workspaces/<id>` - Get a specific workspace
- `PUT /api/workspaces/<id>` - Update a workspace
- `DELETE /api/workspaces/<id>` - Delete a workspace

### Tasks
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/<id>` - Get a specific task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

### Reminders
- `GET /api/reminders` - List all reminders
- `POST /api/reminders` - Create a new reminder
- `GET /api/reminders/<id>` - Get a specific reminder
- `PUT /api/reminders/<id>` - Update a reminder
- `DELETE /api/reminders/<id>` - Delete a reminder

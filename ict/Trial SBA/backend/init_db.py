import pymysql

def create_database_and_tables():
    # Connect without database to create it
    conn = pymysql.connect(
        host='localhost',
        port=3307,
        user='root',
        password='usbw'
    )
    try:
        with conn.cursor() as cur:
            cur.execute("CREATE DATABASE IF NOT EXISTS todo_db")
            print("Database 'todo_db' created or already exists.")
        conn.commit()
    finally:
        conn.close()

    # Connect to todo_db to create tables
    conn = pymysql.connect(
        host='localhost',
        port=3307,
        user='root',
        password='usbw',
        database='todo_db'
    )
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    student_id INT AUTO_INCREMENT PRIMARY KEY,
                    gender VARCHAR(10) NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    form VARCHAR(20) NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS category (
                    category_id INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS workspace (
                    workspace_id INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS task (
                    task_id INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT NOT NULL,
                    category_id INT,
                    workspace_id INT,
                    name VARCHAR(200) NOT NULL,
                    description TEXT,
                    priority VARCHAR(10) NOT NULL DEFAULT 'Medium',
                    completion BOOLEAN NOT NULL DEFAULT FALSE,
                    due_date DATE,
                    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
                    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE SET NULL,
                    FOREIGN KEY (workspace_id) REFERENCES workspace(workspace_id) ON DELETE SET NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS reminder (
                    reminder_id INT AUTO_INCREMENT PRIMARY KEY,
                    task_id INT NOT NULL,
                    reminder_time DATETIME NOT NULL,
                    message VARCHAR(500),
                    FOREIGN KEY (task_id) REFERENCES task(task_id) ON DELETE CASCADE
                )
            """)
            print("All tables created or already exist.")
        conn.commit()
    finally:
        conn.close()

if __name__ == '__main__':
    create_database_and_tables()

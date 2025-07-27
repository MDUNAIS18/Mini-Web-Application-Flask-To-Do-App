Flask To-Do App:
A simple yet beautifully styled To-Do List web application built using Flask and SQLite. This app allows users to add tasks, mark them as complete, delete individual tasks, and clear all tasks with a single click. The interface is clean and user-friendly, designed with sticky-note-style task cards for better usability and visual appeal.

Features:
 * Add new tasks
 * Mark tasks as completed or incomplete
 * Delete individual tasks
 * Clear all tasks at once
 * Clean and colorful sticky notes-style UI
 * SQLite database integration for persistent storage
 * Responsive and modern design using HTML and CSS

Tech Stack:
 * Frontend	Backend	Database
 * HTML5, CSS3	Flask (Python)	SQLite

Project Structure:
cpp
Copy
Edit
Flask-Todo-App/
├── app.py
├── todo.db (auto-generated)
├── templates/
│   └── index.html
└── static/
    └── (optional: for CSS or JS if needed)

Setup Instructions:
1. Clone the Repository:
  bash
  Copy
  Edit
  git clone https://github.com/yourusername/flask-todo-app.git
  cd flask-todo-app

3. Create a Virtual Environment:
  bash
  Copy
  Edit
  python -m venv venv

Activate the environment:

On Windows:
  bash
  Copy
  Edit
  venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate

3. Install Dependencies:
  bash
  Copy
  Edit
  pip install -r requirements.txt
  Or manually:
  bash
  Copy
  Edit
  pip install flask flask_sqlalchemy
4. Run the Application:
  bash
  Copy
  Edit
  python app.py
  Then open your browser and go to:
  http://127.0.0.1:5000

Requirements:
 * Python 3.12.8
 * Flask
 * Flask_SQLAlchemy

Generate requirements.txt using:

  bash
  Copy
  Edit
  pip freeze > requirements.txt
  Database
  The application uses SQLite as the database.

The todo.db file is automatically created on first run and persists the tasks entered.

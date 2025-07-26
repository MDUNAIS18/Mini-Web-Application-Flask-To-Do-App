from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['task']
    if not content.strip():
        return redirect('/')
    new_task = Task(content=content)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    try:
        num_rows_deleted = db.session.query(Task).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Error clearing tasks:", e)
    finally:
        db.session.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

print("Database path:", os.path.abspath('todo.db'))

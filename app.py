from flask import Flask, request, jsonify
from config import DATA_FILE
from repository import TaskRepository
from services import TaskService

app = Flask(__name__)

repo = TaskRepository(DATA_FILE)
service = TaskService(repo)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(repo.get_all())


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    try:
        task = service.create_task(data.get("title"))
        return jsonify(task), 201
    except Exception as e:
        return {"error": str(e)}, 400


@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    task = service.complete_task(task_id)
    if not task:
        return {"error": "task not found"}, 404
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)

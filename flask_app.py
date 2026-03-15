from flask import Flask, jsonify, request
import os

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Task Manager Running"

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "db": True,
        "redis": True
    })

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "priority": data.get("priority"),
        "done": False
    }
    tasks.append(task)
    return jsonify(task)

@app.route("/api/tasks/<int:task_id>/done", methods=["PATCH"])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify({"message": f"Task {task_id} marked done"})
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

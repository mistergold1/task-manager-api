import json
import os
from models import Task


class TaskRepository:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def get_all(self):
        return self.tasks

    def add(self, title):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task.to_dict())
        self._save()
        return task.to_dict()

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save()
                return task
        return None

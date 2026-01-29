from repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, title):
        if not title or len(title) < 3:
            raise ValueError("title too short")
        return self.repo.add(title)

    def complete_task(self, task_id):
        return self.repo.complete(task_id)

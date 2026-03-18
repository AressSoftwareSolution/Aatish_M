class Todo:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        return self.tasks

# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.tags: list = []
        self.completed: bool = False

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos: dict):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str) -> int:
        new_id = len(self.todos) + 1
        new_todo = Todo(new_id, title, description)
        self.todos[new_id] = new_todo
        return new_id

    def pending_todos(self) -> Todo:
        new_list = [todo for todo in self.todos.values() if not Todo.completed]
        return new_list

    def completed_todos(self) -> Todo:
        new_list = [todo for todo in self.todos.values() if Todo.completed]
        return new_list

    def tags_todo_count(self) -> dict:
        tag_count = {}
        for todo in self.todos



import json
class Task:

    def __init__(self, id, description,completed=False):
        self.id = id
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "•" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:
    FILENAME = "task.json"
    def __init__(self):
        self._tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        task = Task(self.next_id, description)
        self._tasks.append(task)
        self.next_id +=1
        self.save_task()
        print(f"Se añadio la taraea {description}")     
    def list_task(self):
        self.load_tasks()
        if not self._tasks:
            print("No ha tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                self.save_task()
                print(f"Tarea completada: {task}")    
                return
        print(f"no se encontro la tarea con id: {id}")
    def delete_task(self,id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                self.save_task()
                print(f"tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")
    
    def load_tasks(self):
        try:
            with open(self.FILENAME,'r') as file:
                data = json.load(file)
                self._tasks = [Task(item["id"],item["description"],item["completed"]) for item in data]
                if self._tasks:
                    self.next_id = self._tasks[-1].id + 1
        except FileNotFoundError:
            self._tasks = []
    
    def save_task(self):
        with open(self.FILENAME,'w') as file:
            json.dump([{"id": task.id,"description": task.description,"completed":task.completed} for task in self._tasks], file, indent=4)
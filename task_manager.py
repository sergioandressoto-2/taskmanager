class Task:

    def __init__(self, id, description,completed=False):
        self.id = id
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "•" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:

    def __init__(self):
        self._tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        task = Task(self.next_id, description)
        self._tasks.append(task)
        self.next_id +=1
        print("Se añadio la taraea {description}")     
    def list_task(self):
        if not self._tasks:
            print("No ha tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")    
                return
        print(f"no se encontro la tarea con id: {id}")
    def delete_task(self,id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")
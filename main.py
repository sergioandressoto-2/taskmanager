from task_manager import TaskManager
def print_menu():
        print("\n --- Gestor de tareas Inteligente ---")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

def main():
    manager = TaskManager()
    
    while True:
        print_menu()
        try:
            option = int(input("Elige una opcion:"))

            match option:
                case 1:      
                    description = input("Descripcion tarea:")
                    manager.add_task(description)
                case 2:
                    manager.list_task()
                case 3:
                    id = int(input("Ingrese numero tarea:"))
                    manager.complet_task(id)
                case 4:
                    id = int(input("Ingrese numero tarea:"))
                    manager.delete_task(id)
                case 5:
                    print("saliendo...")
                    break
                case _:
                    print("option no valida, Seleccione otra")    
        except ValueError:
            print("option no valida, Seleccione otra")
if __name__ == "__main__":
    main()
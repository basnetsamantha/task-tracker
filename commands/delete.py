from utils.file_handler import load_tasks, save_tasks

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print(f"Error: Task with ID {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully.")

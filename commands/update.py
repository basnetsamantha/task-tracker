from utils.file_handler import load_tasks, save_tasks, get_timestamp

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if not new_description.strip():
                print("Error: New description is required.")
                return
            task["description"] = new_description
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task with ID {task_id} not found.")

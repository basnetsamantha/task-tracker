from utils.file_handler import load_tasks, save_tasks, get_timestamp


def mark_in_progress(task_id):
    _update_status(task_id, "in-progress")


def mark_done(task_id):
    _update_status(task_id, "done")


def _update_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

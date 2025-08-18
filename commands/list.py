from utils.file_handler import load_tasks


def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    filtered = tasks
    if filter_status:
        filtered = [t for t in tasks if t["status"] == filter_status]
        if not filtered:
            print(f"No tasks with status '{filter_status}'.")
            return

    for task in filtered:
        print(f"[{task['id']}] {task['description']} ({task['status']})")

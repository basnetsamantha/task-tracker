from utils.file_handler import load_tasks, save_tasks, get_timestamp


def add_task(description):
    if not description.strip():
        print("Error: Description is required.")
        return

    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": get_timestamp(),
        "updatedAt": get_timestamp()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

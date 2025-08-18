import sys
from commands.add import add_task
from commands.update import update_task
from commands.delete import delete_task
from commands.mark import mark_in_progress, mark_done
from commands.list import list_tasks


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python task.py <command> [options]")
        return

    command = args[0]

    if command == "add":
        description = " ".join(args[1:])
        add_task(description)

    elif command == "update":
        if len(args) < 3:
            print("Usage: python task.py update <id> <new description>")
            return
        task_id = int(args[1])
        new_description = " ".join(args[2:])
        update_task(task_id, new_description)

    elif command == "delete":
        if len(args) < 2:
            print("Usage: python task.py delete <id>")
            return
        task_id = int(args[1])
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(args) < 2:
            print("Usage: python task.py mark-in-progress <id>")
            return
        task_id = int(args[1])
        mark_in_progress(task_id)

    elif command == "mark-done":
        if len(args) < 2:
            print("Usage: python task.py mark-done <id>")
            return
        task_id = int(args[1])
        mark_done(task_id)

    elif command == "list":
        if len(args) > 1:
            list_tasks(args[1])
        else:
            list_tasks()

    else:
        print("Unknown command. Use: add, update, delete, mark-in-progress, mark-done, list")


if __name__ == "__main__":
    main()

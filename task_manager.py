import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ---------- File Helpers ----------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def get_new_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1


def current_time():
    return datetime.now().isoformat()


# ---------- Commands ----------
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_new_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": current_time(),
        "updatedAt": current_time()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = current_time()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("⚠️ Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("⚠️ Task not found")
        return
    save_tasks(updated_tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = current_time()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("⚠️ Task not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} "
            f"({task['status']})"
        )


# ---------- CLI ----------
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(sys.argv[2])

        elif command == "update":
            update_task(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress":
            mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            if len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                list_tasks()

        else:
            print("⚠️ Unknown command")

    except IndexError:
        print("⚠️ Missing arguments")
    except ValueError:
        print("⚠️ Invalid ID format")


if __name__ == "__main__":
    main()

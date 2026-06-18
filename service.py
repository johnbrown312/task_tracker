import json
import os
import sys
 
def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r") as f:
        return json.load(f)
 
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)
 
def add_task():
    title = input("Введите описание задачи: ")
    tasks = load_tasks()
    descriptions = [task["description"] for task in tasks]
    if title not in descriptions:
        tasks.append({"id": len(tasks) + 1, "description": title, "status": "todo"})
        save_tasks(tasks)
    list_tasks()
 
def delete_task():
    task_id = int(input("Введите id задачи для удаления: "))
    tasks = load_tasks()
    tasks = [t for t in tasks if t.get("id") != task_id]
    save_tasks(tasks)
    list_tasks()
 
def update_task():
    task_id = int(input("Введите id задачи: "))
    new_description = input("Введите новое описание: ")
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
    save_tasks(tasks)
    list_tasks()
 
def mark_in_progress():
    task_id = int(input("Введите id задачи: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
    save_tasks(tasks)
    list_tasks()
 
def mark_done():
    task_id = int(input("Введите id задачи: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
    save_tasks(tasks)
    list_tasks()
 
def list_tasks(status=None):
    tasks = load_tasks()
    if status is not None:
        tasks = filter(lambda x: x["status"] == status, tasks)
    for task in tasks:
        print(f'{task.get("id")}. {task.get("description")} [{task.get("status")}]')

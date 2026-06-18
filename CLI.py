if len(sys.argv) < 2:
    print("Использование: python task_tracker.py <команда>")
    print("Команды: add, delete, update, mark-in-progress, mark-done, list")
else:
    action = sys.argv[1]
 
    if action == "add":
        add_task()
    elif action == "delete":
        delete_task()
    elif action == "update":
        update_task()
    elif action == "mark-in-progress":
        mark_in_progress()
    elif action == "mark-done":
        mark_done()
    elif action == "list":
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print(f"Неизвестная команда: {action}") 

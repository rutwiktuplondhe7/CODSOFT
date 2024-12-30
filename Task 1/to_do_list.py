tasks = []

def add_task(description):
    task_id = len(tasks) + 1
    task = {'id': task_id, 'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {task_id} - {description}")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    for task in tasks:
        status = "Done" if task['completed'] else "Pending"
        print(f"{task['id']}: {task['description']} - {status}")

def mark_task_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            print(f"Task {task_id} updated to: {new_description}")
            return
    print(f"Task {task_id} not found.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

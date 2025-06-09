todo_list = []

def add_task(task_name):
    task = {"name": task_name, "completed": False}
    todo_list.append(task)
    print(f"Task '{task_name}' added successfully.")

def delete_task(index):
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"Task '{removed_task['name']}' deleted.")
    else:
        print("Invalid task number.")

def display_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(todo_list):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['name']} - {status}")

def mark_task_complete(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print(f"Task '{todo_list[index]['name']}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)

        elif choice == '2':
            display_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            display_tasks()

        elif choice == '4':
            display_tasks()
            try:
                index = int(input("Enter task number to mark complete: "))
                mark_task_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("\nEnter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number - 1] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("\nEnter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4/5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
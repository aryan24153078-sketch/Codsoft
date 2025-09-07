# Simple To-Do List Program in Python

tasks = []

def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("✅ No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"✅ '{task}' added to the list.")

    elif choice == '3':
        if not tasks:
            print("⚠ No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"🗑 '{removed}' removed from the list.")
            except (ValueError, IndexError):
                print("⚠ Invalid task number.")

    elif choice == '4':
        print("👋 Exiting To-Do List. Goodbye!")
        break

    else:
        print("⚠ Invalid choice! Please enter 1-4.")

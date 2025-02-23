import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def display_header():
    header = """
████████╗ ██████╗     ██████╗  ██████╗     ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                                       
"""
    print(header)

def display_menu():
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def main():
    tasks = []

    def add_tasks():
        clear_screen()
        display_header()
        try:
            n_tasks = int(input("\nHow many tasks do you want to add? "))
            for _ in range(n_tasks):
                task = input("Enter the task: ").strip()
                if task:
                    tasks.append({"task": task, "done": False})
                    print("Task added!")
                else:
                    print("Task cannot be empty.")
        except ValueError:
            print("Please enter a valid number.")

    def show_tasks():
        clear_screen()
        display_header()
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_as_done():
        clear_screen()
        display_header()
        if not tasks:
            print("\nNo tasks to mark as done.")
            return

        try:
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    clear_screen()
    display_header()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_tasks()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            clear_screen()
            display_header()
            print("Exiting the To-Do List.")
            break
        else:
            clear_screen()
            display_header()
            display_menu()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

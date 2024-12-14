# Initialize an empty to-do list
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to remove a task from the list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' has been removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the to-do list
def display_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")

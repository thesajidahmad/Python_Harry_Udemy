tasks = []

def view_task():
    print(f"\n{tasks}\n")

def add_task():
    total_task = int(input("How many task you want to add: "))
    for i in range(1, total_task+1):
        new_task = input(f"Enter Task {i}: ")
        tasks.append(new_task)

def update_task():
    old_task = input("Enter which task do you want to update: ")
    if old_task in tasks:
        updated_task = input("Enter the new updated task: ")
        indx = tasks.index(old_task)
        tasks[indx] = updated_task

def delete_task():
    del_task = input("Enter the task you want to delete: ")

    if del_task in tasks:
        indx = tasks.index(del_task)
        tasks.pop(indx)

def main():
    print("\n---Welcome to Task Management Application---\n")
    # print(tasks)
    while True:
        choice = int(input("Enter 1 for View Tasks\nEnter 2 for Add\nEnter 3 for Update\nEnter 4 for Delete\nEnter 5 for Exit\nEnter your choice: "))

        match choice:
            case 1:
                view_task()
            case 2:
                add_task()
            case 3:
                update_task()
            case 4:
                delete_task()
            case 5:
                break
            case _:
                print("Invalid Input!!")

if __name__ == "__main__":
    main()
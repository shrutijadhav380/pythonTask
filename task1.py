todo_list=[]

#Functioon to add A New Task 
def add_task():
    task = input("enter a task")
    todo_list.append({"Task":task,"Status":"pending"})
    print("New Task Added Successfully!")


#Functioon to view All Task 
def view_task():
    print("your todo list:")
    if len(todo_list)==0:
        print("No pending list")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}.{task['Task']} - {task['Status']}")
    print("\n")


#Functioon to remove a Task 
def remove_task():
    if len(todo_list)==0:
        print("List is empty")
    else:
        try:
            search_index=int(input("enter the task Number to remove:")) -1
            if 0 <=search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("please enter a valid number.")

#Function to mark a TAsk as Done
def mark_done():
    if len(todo_list)==0:
        print("List is empty")
    else:
        try:
            search_index=int(input("enter the task Number to remove:")) -1
            if 0 <=search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task '{todo_list[search_index]['Task']}'marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("please enter a valid number.")

#Menu function 
def menu():
    while True:
        print("\n1. Add new task")
        print("2.View All Tasks")
        print("3.Remove a Tasks")
        print("4.Mark a Task as Completed")
        print("5.Exit")

        choice=input("Enter Your choice:")
        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            mark_done()
        elif choice=="5":
            print("Exiting the application ")
            break
        else:
            print("Invalid choice! Try again.")
#Run the program 
menu()
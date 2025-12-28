tasks=[]
while True:
    print("TO DO LIST")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.EXIT")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter the task to add:")
        tasks.append(task)
        print("Task added successfully")
    elif choice==2:
        if len(tasks)==0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
    elif choice==3:
        if len(tasks)==0:
            print("Not found")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
            task_number=int(input("Enter the task number to Remove:"))
            if task_number>0 and task_number<=len(tasks):
                tasks.pop(task_number-1)
                print("Task Removed Successfully")
            else:
                print("Invalid task number")
    elif choice==4:
        print("Exiting To-Do list.Bye!")
        break
    else:
        print("Invalid choice.please try again")
            
            
            

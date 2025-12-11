tasks = []

while True:
    print()
    print("To-do list program😃-->")
    print("which task yo want to chose\n1-Add task\n2-See task\n3-Delete tasks\n4-Exit\n5-tick\n6-Update")
    choice = int(input("Enter the task number💪🏻 :"))
    
    if (choice==1):
        task = input("enter the task:")
        tasks.append(task)
        print("task added👍🏻")
    
    elif (choice==2):
        if not tasks:
            print("not tasks yet🙄")
        else:
            for i,t in enumerate(tasks,start=1):
                print(i,"-",t)

    elif (choice==3):
        if not tasks:
            print("not tasks to remove🫤")
        else:
            for num in tasks:
                removed=tasks.remove(num)
            print("tasks deleted👍🏻")

    elif choice==4:
        print("Thanks for using🥰")
        break
    
    elif choice==5:
        to_tick= input("which task you want to tick🥱 :")
        if to_tick in tasks:
            ind= tasks.index(to_tick)
            tasks[ind]= to_tick+"✅"
        else:
            print("invalid argument🤫")
    
    elif(choice==6):
        task_up = input("which task you want to update:")
        if task_up in tasks:
            new_task= input("enter new task:")
            ind_old = tasks.index(task_up)
            tasks[ind_old]=new_task
            print("task updated🤠")
        else:
            print("this task is not valid🙄")

    else:
        print("invalid syntax😝")
        print("please try again☺️")
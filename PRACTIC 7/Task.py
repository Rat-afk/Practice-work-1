import json, datetime, sys

def add():
    task = {}

    title = input("Please Enter a Title of the Task or Enter Nothing to Exit to Main Menu: ")
    if title == '':
        print()

        main()

    task["Title"] = title

    desc = input("Please Enter a Description of the Task: ")
    task["Description"] = desc

    while True:
        try:
            deadline = input("Please Enter a Deadline of the Task in Format dd.mm.yyyy: ")

            datetime.datetime.strptime(deadline, "%d.%m.%Y")
            task["Deadline"] = deadline

            break
        except ValueError:
            print("Invalid Date Format. Please Try Again" + '\n')

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []

            tasks.append(task)
            file.seek(0)
            json.dump(tasks, file, indent =4)
            file.truncate()

            print("Task Added Successfully" + '\n')
    except FileNotFoundError:
        with open("tasks.json", 'w') as file:
            json.dump([task], file, indent = 4)

    main()

def remove():
    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Select Task to Remove (Enter Number of the Task) or Enter 0 to Exit to Main Menu:")

            for task in range (len(tasks)):
                print(task + 1, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

            print()

            while True:
                try:
                    task_remove = int(input("Task to Remove: "))

                    if task_remove == 0:
                        print()

                        main()

                    if (task_remove < 0) or (task_remove > len(tasks)):
                        print("Invalid Number. Please Try Again" + "\n")

                        continue

                    break
                except ValueError:
                    print("Invalid Number. Please Try Again" + "\n")

                    continue

            tasks.pop(task_remove - 1)

            file.seek(0)
            file.truncate()

            json.dump(tasks, file, indent = 4)

            print("Task Removed Successfully" + '\n')
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def edit():
    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Select Task to Edit (Enter Number of the Task) or Enter 0 to Exit to Main Menu:")

            for task in range (len(tasks)):
                print(task + 1, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

            print()

            while True:
                try:
                    task_edit = int(input("Task to Edit: "))

                    if task_edit == 0:
                        print()

                        main()

                    if (task_edit < 0) or (task_edit > len(tasks)):
                        print("Invalid Number. Please Try Again" + "\n")

                        continue

                    break
                except ValueError:
                    print("Invalid Number. Please Try Again" + "\n")

                    continue

            print("What Would You Like to Change in the Task")
            print("1 - Change Title" + '\t' + "2 - Change Description" + '\t' + "\t3 - Change Deadline")

            while True:
                try:
                    change = int(input("To Change: "))

                    if (change < 1) or (change > 3):
                        print("Invalid Number. Please Try Again" + "\n")

                        continue

                    break
                except ValueError:
                    print("Invalid Number. Please Try Again" + "\n")

                    continue

            if change == 1:
                tasks[task_edit - 1]["Title"] = input("Please Enter a New Title of the Task: ")
            elif change == 2:
                tasks[task_edit - 1]["Description"] = input("Please Enter a New Description of the Task: ")
            else:
                while True:
                    try:
                        deadline = input("Please Enter a New Deadline of the Task in Format dd.mm.yyyy: ")

                        datetime.datetime.strptime(deadline, "%d.%m.%Y")
                        tasks[task_edit - 1]["Deadline"] = deadline

                        break
                    except ValueError:
                        print("Invalid Date Format. Please Try Again" + "\n")

            file.seek(0)
            json.dump(tasks, file, indent=4)
            file.truncate()
            file.close()

            print("Task Edited Successfully" + '\n')
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def today():
    number = 1

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Tasks for Today:")

            for task in range (len(tasks)):
                if tasks[task]["Deadline"] == datetime.datetime.strftime(datetime.datetime.today(), "%d.%m.%Y"):
                    print(number, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

                    number += 1

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def tomorrow():
    number = 1

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Tasks for Tomorrow:")

            for task in range (len(tasks)):
                if tasks[task]["Deadline"] == datetime.datetime.strftime(datetime.datetime.today() + datetime.timedelta(days = 1), "%d.%m.%Y"):
                    print(number, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

                    number += 1

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def week():
    number = 1
    days_week = 7

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Tasks for the Week:")

            for task in range (len(tasks)):
                if (tasks[task]["Deadline"] < datetime.datetime.strftime(datetime.datetime.today() + datetime.timedelta(days = days_week), "%d.%m.%Y")) and \
                        (tasks[task]["Deadline"] >= datetime.datetime.strftime(datetime.datetime.today(), "%d.%m.%Y")):
                    print(number, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

                    number += 1

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def all_tasks():
    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("All Tasks:")

            for task in range (len(tasks)):
                print(task + 1, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def future():
    number = 1

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Future Tasks:")

            for task in range (len(tasks)):
                if tasks[task]["Deadline"] >= datetime.datetime.strftime(datetime.datetime.today(), "%d.%m.%Y"):
                    print(number, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

                    number += 1

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def past():
    number = 1

    try:
        with open("tasks.json", 'r+') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No Tasks Found" + '\n')

                main()

            if not tasks:
                print("No Tasks Found" + '\n')

                main()

            print("Past Tasks:")

            for task in range (len(tasks)):
                if tasks[task]["Deadline"] < datetime.datetime.strftime(datetime.datetime.today(), "%d.%m.%Y"):
                    print(number, "-> Title:", tasks[task]["Title"], '\t', "\tDescription:", tasks[task]["Description"], '\t', "\tDeadline:", tasks[task]["Deadline"])

                    number += 1

            print()
    except FileNotFoundError:
        print("Tasks Not Found" + '\n')

    main()

def main():
    print("Welcome to the Diary App Main Menu. Please Select an Action:")
    print("1 - Add Task" + '\t' + "3 - Edit Task" + '\t' + "5 - View Tasks for Tomorrow\t" + '\t' + "7 - View All Tasks\t" + '\t' + "9 - View Past Tomorrow")
    print("2 - Remove Task\t" + '\t' + "4 - View Tasks for Today" + '\t' + "6 - View Tasks for the Week\t" + '\t' + "8 - View Future Tasks" + '\t' + "0 - Close The App\n")

    while True:
        try:
            choose = int(input("Please Select an Action: "))

            if (choose < 0) or (choose > 9):
                print("Invalid value. Please Try Again" + '\n')

                continue

            break
        except ValueError:
            print("Invalid value. Please Try Again" + '\n')

    if choose == 1:
        add()

    elif choose == 2:
        remove()

    elif choose == 3:
        edit()

    elif choose == 4:
        today()

    elif choose == 5:
        tomorrow()

    elif choose == 6:
        week()

    elif choose == 7:
        all_tasks()

    elif choose == 8:
        future()

    elif choose == 9:
        past()

    else:
        sys.exit()

main()

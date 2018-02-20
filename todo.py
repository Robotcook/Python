print "Welcome to the TODO task management program."

task_dict = {}

while True:
    task = raw_input("Please enter TODO task: ")
    status = raw_input("Was the task completed yet? (yes/no)")
    print "Your task is: " + task

    if status == "yes":
        task_dict[task] = True
    else:
        task_dict[task] = False

    new = ""
    while new !="yes" and new != "no":
        new = raw_input("Would you like to enter a new task? (yes/no) ").lower()

    if new == "no":
        break

print("Completed tasks:")

for task in task_dict:
    if task_dict[task] is True:
        print[task]

print("Open tasks:")

for task in task_dict:
    if task_dict[task] is False:
        print[task]

with open("todo.txt", "w+") as todo_file:
    for task in task_dict:
        todo_file.write(task + " - " + str(task_dict[task]) + "\n")
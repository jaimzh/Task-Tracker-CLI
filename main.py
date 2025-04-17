import datetime

taskList =[ 
    
]


def help():
    print("""
Available Commands:
---------------------
1. add <task_description> - Adds a new task with the given description.
   Example: add Buy groceries

2. delete <task_id> - Deletes the task with the given task ID.
   Example: delete 1

3. update <task_id> <new_description> - Updates the description of the task with the given ID.
   Example: update 2 Study React

4. mark-in-progress <task_id> - Marks the task with the given ID as 'in progress'.
   Example: mark-in-progress 3

5. mark-done <task_id> - Marks the task with the given ID as 'done'.
   Example: mark-done 2

6. list - Lists all tasks with their current statuses.

7. list-done - Lists all tasks that are marked as 'done'.

8. list-in-progress - Lists all tasks that are marked as 'in progress'.

9. list-todo - Lists all tasks that are still 'todo'.

10. exit - Exits the application.
""")

# handle commands
def handle_commands(arg, task_id=None,  description=None):
    if arg == 'add':
        add_task(description)
    elif arg == 'delete':
        delete_task(task_id) 
    elif arg == 'update':
        update_task(task_id, description)
    elif arg == 'mark-in-progress':
        mark_in_progress(task_id)
    elif arg == 'mark-done':
        mark_done(task_id)
    elif arg == 'mark-todo':
        mark_todo(task_id)
    else:
        print("wrong command")

    
# this is the list section that shows done, inprogress and to do list 


def done_list():
    done_tasks = [task for task in taskList if task['task_status'] == 'done']
    print(done_tasks)


def inprogress_list():
    inprogress_tasks = [task for task in taskList if task['task_status'] == 'in progress']
    print(inprogress_tasks)

def todo_list():
    todo_tasks = [task for task in taskList if task['task_status'] == 'todo']
    print(todo_tasks)
        
# this is the mark section, that marks inprogress and mark done tasks
def mark_in_progress(task_id):
    task_id = int(task_id)
    for task in taskList:
        if task['task_id'] == task_id:
            task['task_status'] = 'in progress'
            print(f'Task {task_id} marked as in progress')
            return
    print('we gotta problem')
         
def mark_done(task_id):
    task_id = int(task_id)
    for task in taskList:
        if task['task_id'] == task_id:
            task['task_status'] = 'done'
            print(f'Task {task_id} is marked as  done')
            return
    print('we gotta problem')
    
def mark_todo(task_id):
    task_id = int(task_id)
    for task in taskList:
        if task['task_id'] == task_id:
            task['task_status'] = 'todo'
            print(f'Task {task_id} is marked as todo')
            return
    print('we gotta problem')
    
     
# this is the add, delete, and update section   
def add_task(description): 
    new_task ={
        "task_id": len(taskList)+1,
        "task_description": description,
        "task_status": "todo",
        "date_created": getcurrent_date() ,
        "date_updated": getcurrent_date()
    }    
    taskList.append(new_task)
    print(f"Task added: {new_task['task_id']}")
    
def delete_task(task_id):
    task_id = int(task_id)
    for task in taskList:
        if task["task_id"] == task_id:
            taskList.remove(task)
            print(f"Task {task_id} deleted")
            return
    print(f"Task {task_id} not found")

def update_task(task_id, description):
    task_id = int(task_id)
    for task in taskList:
        if task["task_id"] == task_id:
            task["task_description"] = description
            task["date_updated"] = getcurrent_date()
            print(f"Task {task_id} updated")
            return
    print(f"Task {task_id} not found")
   
# date hander
def getcurrent_date():
    date_time = datetime.datetime.now()
    date= date_time.date()
    time= date_time.time().strftime("%H:%M %p")
    return (f"{date} by {time}")
  


            
if __name__ == "__main__":
    print("START TYPING")
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            print('you exited')
            break
        if user_input == "list":
            print(taskList)
        if user_input.startswith('add'):
            commands, description = user_input.split(" ", 1)
            handle_commands(commands, description)       
        if user_input.startswith('delete'):
            commands, task_id = user_input.split(" ", 1)
            handle_commands(commands, task_id)
        if user_input.startswith('update'):
            commands, task_id, description = user_input.split(" ", 2)
            handle_commands(commands, task_id, description)
        if user_input.startswith('mark-in-progress'):
            commands, task_id = user_input.split(" ", 1)
            handle_commands(commands, task_id)
        if user_input.startswith("mark-done"):
            commands, task_id = user_input.split(" ", 1)
            handle_commands(commands, task_id)
        if user_input.startswith("mark-todo"):
            commands, task_id = user_input.split(" ", 1)
            handle_commands(commands, task_id)
        if user_input.startswith("list-done"):
            done_list()
        if user_input.startswith("list-in-progress"):
            inprogress_list()
        if user_input.startswith("list-todo"):
            todo_list()
        if  user_input.startswith("help"):
            help()
        

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action or "more" in user_action:
        todo = user_action[4:] + "\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif "show" in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        #new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif "complete" in user_action:
        number = int(user_action[9:])
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number-1)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif "edit" in user_action:
        number = int(user_action[5:]) - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break
    else:
        print("Command Invalid")
print("Bye")

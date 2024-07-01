def get_todos():
    with open('files/todos.txt', 'r') as file_l:
        todos_local = file_l.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos()

        todos.append(todo)
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number-1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Your value is not a valid number")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command Invalid")
print("Bye")

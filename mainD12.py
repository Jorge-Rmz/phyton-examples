def get_todos(filepath):
    with open(filepath, 'r') as file_l:
        todos_local = file_l.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action.isupper();
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos('files/todos.txt')

        todos.append(todo)
        write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos('files/todos.txt')
        # new_todo = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos('files/todos.txt')

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number-1)

            write_todos("files/todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Your value is not a valid number")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("files/todos.txt", todos)

        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command Invalid")
print("Bye")



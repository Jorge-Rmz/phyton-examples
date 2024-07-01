
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case "show":
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            #new_todo = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}-{item}")

        case "complete":
            number = int(input("Number of the todo to complete: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number-1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove.strip} was removed from the list"
            print(message)

        case "edit":
            number = int(input("Enter the number for edit: ")) - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "exit":
            break
print("Bye")

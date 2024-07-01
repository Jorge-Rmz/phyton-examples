
while True:
    user_action = input("Type add, show, edit, complete or exit: ");
    user_action = user_action.strip();
    match user_action:
        case "add":
            todo = input("Enter a todo: ")+ "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index+1}-{item}")

        case "complete":
            number = int(input("Number of the todod to complete"))
            todos.pop(number-1)
        case "edit":
            number = int(input("Enter the number for edit: ")) -1
            todos[number] = input("Enter your new todo")
        case "exit":
            break
print("Bye")
date = input("Enter today's date: ")
mood = input("Enter to you rate mood today from 1 to 10? ")

journal = input('Let your thoughts flow: \n')

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(journal)

import csv

with open("files/mainCSV/weather.csv", "r") as file:
    data = list(csv.reader(file))


print(data)
city = input("Enter city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])



print("The city isn't in the list. ")
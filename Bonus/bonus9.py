password = input("Enter your new password")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
uppercase = False
for item in password:
    if item.isdigit():
        digit = True
    if item.isupper():
        uppercase = True

result.append(digit)
result.append(uppercase)

if all(result):
    print("The password is valid")
else:
    print("The password is wrong")


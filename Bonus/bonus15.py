import json

with open("question.json", "r") as file:
    content = file.read()

data = json.loads(content)
# print(data)
for question in data:
    print(question["question_text"])
    for number, index in enumerate(question["alternatives"]):
        print(f"{number+1}-{index}")
    question["user_choice"] = int(input("Select the answer correctly: "))


score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Response is correct"
    else:
        result = "Wrong answer"
    message = f"{result} {index+1} - your Answer {question['user_choice']}, " \
              f"Correct Answer: {question['correct_answer']}"
    print(message)

print(f"Your score is {score} of 2")
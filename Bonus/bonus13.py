def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet , "inches": inches }


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])

if result < 1:
    print("Kid is too small. ")
else:
    print("Kid can use the slide.")


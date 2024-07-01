from Bonus.parsers14 import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])

if result < 1:
    print("Kid is too small. ")
else:
    print("Kid can use the slide.")


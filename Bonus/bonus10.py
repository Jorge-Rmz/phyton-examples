try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    if width == length :
        exit("Both values cannot be the same.")
    else:
        area = width * length

        perimeter = (width + length) * 2

        print(area, perimeter)

except ValueError:
    print("Enter a number, please: ")
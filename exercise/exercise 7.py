filesname = ["a.txt", "b.txt", "c.txt"]
ruta_special = "../files/exercise 7/"

for item in filesname:
    file = open(f"{ruta_special}{item}", "r")
    print(file.read())
    file.close()


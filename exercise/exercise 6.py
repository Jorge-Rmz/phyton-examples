filenames = ['doc.txt', 'report.txt', 'presentation.txt']
directory_special = "../files/exercise 6/"
for filename in filenames:
    file = open(f"{directory_special} {filename}", 'w')
    file.write("Hello")
    file.close()
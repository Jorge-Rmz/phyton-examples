import glob

files = glob.glob("files/filesfake/*.txt")

for filepath in files:
    print(filepath)
filesnames = ["1.doc","2.report", "3.presentation"]

filesnames = [filename.replace(".", "-") + ".txt" for filename in filesnames]

print(filesnames)
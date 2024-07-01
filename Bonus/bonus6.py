contens = ["Este es el contenido 1", "Este es el contenido 2", "Este es el contenido 3"]

filesnames = ["doc.txt", "report.txt", "presentation.txt"]

for conten, filesname in zip(contens, filesnames):
    file = open(f"../files/{filesname}", "w")
    file.write(conten)
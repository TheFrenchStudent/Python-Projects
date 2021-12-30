# Programme permettant d'effectuer une rotation à 90° d'un fichier pdf nommé test.pdf.

import PyPDF2

with open("test.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

# Autre programme sur le même principe permettant de combiner plusieurs fichiers pdf (ici first et second) en un seul appelé combined.pdf.

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")

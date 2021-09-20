import PyPDF2
from pdfops import opmap

file = open("Python.pdf", 'rb')
pdf = PyPDF2.PdfFileReader(file)

print("What would you like to do with this PDF?\n")
print("1. Get number of pages in the PDF")
print("2. Get information about the PDF")
print("3. Get page layout of the PDF")
print("4. Get page mode of the PDF")
print("5. Read a specific page from the PDF")
print("6. Check if the PDF is encrypted")

choice = input("\nYour choice: ")

while choice in opmap.keys():
    opmap[choice](pdf)
    choice = input("\nYour choice: ")
else:
    print("So you're leaving me like everyone else too?")

file.close()

from pypdf import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("how many pdf do you wnat to merge "))

for i in range(0,n):
    name=print(f"enter the name of  pdf {i+1}")
    pdfs.append(name)


for pdf in pdfs:
    merger.append(pdf)

merger.write("meged-pdf.pdf")
merger.close()

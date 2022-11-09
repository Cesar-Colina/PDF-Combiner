import PyPDF2

PDF1 = open(r'PDF file path','rb')
PDF2 = open(r'PDF2 file path','rb')

PDF1R = PyPDF2.PdfFileReader(PDF1)
PDF2R = PyPDF2.PdfFileReader(PDF2)

writer = PyPDF2.PdfFileWriter()

for pagenum in range(PDF1R.numPages):
    page = PDF1R.getPage(pagenum)
    writer.addPage(page)

for pagenum in range(PDF2R.numPages):
    page = PDF2R.getPage(pagenum)
    writer.addPage(page)

pdfOutput = open('New PDF name', 'wb')
writer.write(pdfOutput)
pdfOutput.close()

#for pagenum in range(PDF1R.numPages):
#    print(PDF2R.getPage(pagenum).extractText())

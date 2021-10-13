'''
The PyPDF2 module can read and write PDFs.
Opening a PDF is done by calling open() and passing the file object to PPdfFileReader().
A Page object can be obtained from the PDF object with the getPage() method.
The text from a Page object is obtained with the extractText() method, which can be imperfect.
New PDFs can be made from PdfFileWriter().
New pages can be appended to a writer object with the addPage() method.
Call the write() method to save its changes.
'''

import PyPDF4

# pdfFile = open('meetingminutes1.pdf', 'rb')
#
# reader = PyPDF4.PdfFileReader(pdfFile)
# print(reader.numPages)
#
# page = reader.getPage(0)
# print(page.extractText())

# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

pdf1 = open('meetingminutes1.pdf', 'rb')
pdf2 = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF4.PdfFileReader(pdf1)
reader2 = PyPDF4.PdfFileReader(pdf2)

writer = PyPDF4.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputfile = open('combinedminutes.pdf', 'wb')
writer.write(outputfile)
outputfile.close()
pdf1.close()
pdf2.close()

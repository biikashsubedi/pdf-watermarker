import PyPDF2

template = PyPDF2.PdfFileReader(open('./super.pdf', 'rb'))
watermaker = PyPDF2.PdfFileReader(open('./wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermaker.getPage(0))
    output.addPage(page)

    with open('watermark_output.pdf', 'wb') as file:
        output.write(file)

import PyPDF2
object = open('file.pdf', 'rb')
txt_file = open('out_put.txt', 'w')
reader = PyPDF2.PdfFileReader(object)
total_pages = reader.numPages
i = 0
for i in range(total_pages):
    page = reader.getPage(i)
    line = page
    page_content = page.extractText()
    #print('page', type(page))
    print(page_content.encode('utf8'))





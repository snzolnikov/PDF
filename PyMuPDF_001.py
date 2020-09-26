# данная библиотека хорошо работает с кирилицей!

import fitz

pdf_document = "file.pdf"
txt_document = "file.txt"

doc = fitz.open(pdf_document) # открываем на чтение файл PDF
txt = open(txt_document, 'w') # открываем на запись (создаем новый) текстовый файл
total_pages = doc.pageCount   # получаем количество страниц PDF документа
# print("number of pages: %i" % doc.pageCount) # выводим количество страниц
print(doc.metadata)     # информация о файле PDF
                        # {'format': 'PDF 1.4', 'title': None, 'author': None,
                        # 'subject': None, 'keywords': None, 'creator': None,
                        # 'producer': 'Ghostscript 8.70', 'creationDate': "D:20160322120618+03'00'",
                        # 'modDate': "D:20160322120618+03'00'", 'encryption': None}
for i in range(0, total_pages):
    page1 = doc.loadPage(i)
    page1text = page1.getText("text")
    #print(type)
    #print(page1text)
    lines = page1text.split('\n')  # можно из текста сделать list
    txt.write(page1text)  # записываем в файл txt полученный из PDF файла текст
    #print(type(lines))
txt.close()  # закрываем текстовый файл
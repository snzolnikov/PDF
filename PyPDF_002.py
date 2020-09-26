#!/usr/bin/python
from PyPDF2 import PdfFileReader

pdf_document = "file.pdf"
with open(pdf_document, "rb") as filehandle:
   pdf = PdfFileReader(filehandle)
   info = pdf.getDocumentInfo()
   pages = pdf.getNumPages()
   print('file information: ', info)
   print("number of pages: %i" % pages)
   page1 = pdf.getPage(0)
   print(pdf.getIsEncrypted())
   print(pdf.pageMode)
   print(pdf.getFields())
   print(pdf.stream)
   print(pdf.flattenedPages)
   print(page1)
   print(page1.extractText())
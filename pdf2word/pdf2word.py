import PyPDF2
import os

'''
APP_PATH=os.getcwd()
FILE_PATH = 'C://Users//PC//Desktop//power_china//'+'cert_activos.pdf'
with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(1)
    print(page.extractText())


pdf_file = open("C://Users//PC//Python//Ejercicios//pdf2word//cert_activos.pdf", "rb").read().decode("latin-1")
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content)
'''

# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open("C://Users//PC//Python//Ejercicios//pdf2word//cert_activos.pdf", 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.getPage(0) 
    
# extracting text from page 
print(pageObj.extractText()) 
    
# closing the pdf file object 
pdfFileObj.close() 
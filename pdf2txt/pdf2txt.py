#pip install pdfminer.six

# Replace 'input.pdf' with the path to your PDF file and 'output.txt' with the desired text file name
pdf_path = 'input.pdf'
txt_path = 'output.txt'

import pdfminer
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def pdf_to_txt(pdf_path, txt_path):
    output_string = StringIO()
    
    try:
        with open(pdf_path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        
        # Obtener el texto extraído y eliminar las líneas vacías
        text = output_string.getvalue()
        text_without_empty_lines = "\n".join([line for line in text.splitlines() if line.strip()])
        
        # Escribir el texto sin líneas vacías en un archivo
        with open(txt_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text_without_empty_lines)
        
        print(f"Text extracted and saved to {txt_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        output_string.close()

pdf_to_txt(pdf_path, txt_path)

from PyPDF2 import PdfReader
import openpyxl

def extract_text_from_pdf(pdf_file_path):
    text_lines = []
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            page_lines = page_text.split('\n')
            text_lines.extend(page_lines)
    return text_lines

def write_text_to_excel(text_lines, excel_file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'PDF Text'
    for row_num, line in enumerate(text_lines, start=1):
        sheet.cell(row=row_num, column=1, value=line)
    workbook.save(excel_file_path)

# Example usage
pdf_file_path = 'articulosxr.pdf'
excel_file_path = 'extracted_text.xlsx'

text_lines = extract_text_from_pdf(pdf_file_path)
write_text_to_excel(text_lines, excel_file_path)
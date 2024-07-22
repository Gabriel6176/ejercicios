from PyPDF2 import PdfReader
import openpyxl

def extract_text_from_pdf_and_split_to_excel(pdf_file_path, output_excel_name):
    # Load the Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'PDF Text'

    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        
        # Iterate through each page of the PDF
        for page_num, page in enumerate(reader.pages, start=1):
            # Extract text from the page
            page_text = page.extract_text()
            
            # Split text into lines
            page_lines = page_text.split('\n')
            
            # Iterate through each line
            for line in page_lines:
                
                split_line = line.strip()
                                
                # Write the split information into separate columns in the output workbook
                row_num = len(sheet['A']) + 1  # Find the next empty row in column A
                sheet.cell(row=row_num, column=1, value=split_line)
                
    
    # Save the output workbook
    workbook.save(output_excel_name)

# Example usage
pdf_file_path = 'Lista de precios Winhouse 2024.pdf'
output_excel_name = 'processed_data_23.xlsx'
extract_text_from_pdf_and_split_to_excel(pdf_file_path, output_excel_name)
print('Proceso Finalizado')
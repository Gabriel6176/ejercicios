import fitz  # PyMuPDF
import os

# Example usage
var_input = "OP 7336"
input_pdf = var_input + ".pdf"
output_pdf = var_input + "_comp.pdf"

def compress_pdf(input_path, output_path, zoom_x=0.5, zoom_y=0.5, rotation=0):
    """
    Compress a PDF file.
    
    Parameters:
    - input_path: str, the path to the input PDF file.
    - output_path: str, the path to save the compressed PDF file.
    - zoom_x: float, the zoom factor in the horizontal direction (default is 0.5).
    - zoom_y: float, the zoom factor in the vertical direction (default is 0.5).
    - rotation: int, the rotation in degrees (default is 0).
    """
    try:
        # Open the input PDF file
        document = fitz.open(input_path)
        
        # Create a new PDF document for the output
        new_document = fitz.open()
        
        # Iterate over each page
        for page_num in range(len(document)):
            # Get the page
            page = document.load_page(page_num)
            
            # Set the transformation matrix for zoom and rotation
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation)
            
            # Get the transformed page
            pix = page.get_pixmap(matrix=mat)
            
            # Add the page to the new document
            new_page = new_document.new_page(width=pix.width, height=pix.height)
            new_page.insert_image(new_page.rect, pixmap=pix)
        
        # Save the compressed PDF
        new_document.save(output_path)
        print(f"PDF compressed successfully and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Compress the PDF
compress_pdf(input_pdf, output_pdf)




from PyPDF2 import PdfMerger
import os

APP_PATH=os.getcwd()

pdfs = [APP_PATH+'//'+'PC12.pdf', APP_PATH+'//'+'PC3.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(APP_PATH+"//"+"Powerchinafinal.pdf")
merger.close()
print("FINALIZO CON EXITO")
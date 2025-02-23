from PyPDF4 import PdfFileMerger
import os

def merge_pdfs():
    pdf_files = [item for item in os.listdir() if item.endswith('.pdf') and item != 'Final_pdf.pdf']
    
    if len(pdf_files) == 0:
        print("No PDF files found to merge. Please give PDF to work.")
        return
    
    print(f"Number of PDF files found: {len(pdf_files)}")
    
    merger = PdfFileMerger()
    
    try:
        for item in pdf_files:
            merger.append(item)
        
        output_filename = "Final_pdf.pdf"
        merger.write(output_filename)
        print("PDF merge complete.")
    
    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
    
    finally:
        merger.close()

def remove_old_pdfs():
    pdf_files = [item for item in os.listdir() if item.endswith('.pdf') and item != 'Final_pdf.pdf']
    
    if len(pdf_files) == 0:
        return
    
    try:
        for item in pdf_files:
            os.remove(item)
        
        print("Old PDF files removed.")
    
    except Exception as e:
        print(f"An error occurred while removing old PDFs: {e}")

if __name__ == "__main__":
    merge_pdfs()
    remove_old_pdfs()

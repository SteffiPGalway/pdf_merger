from PyPDF2 import PdfMerger
import logging
import os


logging.basicConfig(
    filename= 'merge_pdf.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
MERGED_FILE = 'merged.pdf'


def check_pdfs(input_dir: str) -> list:
    '''
    Checks if files in INPUR_DIR is a pdf file
    Logs the number pdf files found in the directory
    Args:
        INPUT_DIR
    Returns:
        pdf_files (list)
    '''

    pdf_files = []
    for filename in os.listdir(input_dir):
        lower_filename = filename.lower()
        if not lower_filename.endswith('.pdf'):
            logging.warning("No PDF files found in the input directory.")
        else:
            pdf_files.append(filename)
            logging.info(f"Found {len(pdf_files)} PDF files: {pdf_files}")
    return pdf_files

def merge_pdfs(pdf_files: str, input_dir: str, output_dir: str, output_filename: str) -> None:
    '''
    Merge PDF files from the input directory into a single PDF file.
    Logs the process of merging and any errors encountered.
    Args:
        pdf_files (list): List of PDF files to merge.
        input_dir (str): Directory containing the PDF files.
        output_dir (str): Directory to save the merged PDF file.
        output_filename (str): Name of the merged PDF file.
    Returns:
        None
    '''
    merger = PdfMerger()
    logging.info("Starting PDF merge process.")
    for pdf in pdf_files:
        pdf_path = os.path.join(input_dir, pdf)
        try:
            merger.append(pdf_path)
            logging.info(f"Appended '{pdf}' successfully.")
        except Exception as e:
            logging.error(f"Failed to append '{pdf}': {e}")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    try:
        merger.write(output_path)
        logging.info(f"Merged PDF saved to '{output_path}'.")
    except Exception as e:
        logging.error(f"Failed to write merged PDF: {e}")
    finally:
        merger.close()

if __name__ == '__main__':
    pdf_files = check_pdfs(INPUT_DIR)
    if pdf_files:
        merge_pdfs(pdf_files, INPUT_DIR, OUTPUT_DIR, MERGED_FILE)
    else:
        logging.info("No PDF files to merge.")

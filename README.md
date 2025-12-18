# PDF Merger App

A simple Python application to merge two or more PDF files from an **input** folder into a single PDF in an **output** folder. The application uses [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF handling and Python's built-in `logging` for logging activities.

## Installation

```bash

# Clone the repository
git clone https://github.com/SteffiPGalway/pdf_merger.git
cd pdf_merger

# Install dependencies in active Python environment
pip install -r requirements.txt

# run script directly 
python3 merge_pdf.py

# run via helper script 
./run_pdf_merger.sh
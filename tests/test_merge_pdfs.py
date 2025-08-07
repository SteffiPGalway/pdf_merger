import os
import PyPDF2

def test_merge_pdfs_from_files(tmp_path):
    # Paths to PDFs
    file1 = os.path.join("tests", "File1.pdf")
    file2 = os.path.join("tests", "File2.pdf")

    # Merge the two PDFs
    merger = PyPDF2.PdfMerger()
    merger.append(file1)
    merger.append(file2)

    # Output file (in temporary test directory)
    output_path = tmp_path / "merged.pdf"
    with open(output_path, "wb") as f:
        merger.write(f)
    merger.close()

    # Assert the merged PDF has the correct number of pages
    with open(output_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        assert len(reader.pages) == 2
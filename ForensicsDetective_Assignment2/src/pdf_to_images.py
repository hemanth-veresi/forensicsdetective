# pdf_to_images.py
# ----------------------------------------------------
# Converts all PDFs into image files (.png)
# Each PDF page is turned into one image.
# We'll save all images under data/images/

import os
import fitz  # PyMuPDF
from tqdm import tqdm

def convert_pdfs_to_images(input_dir="data/generated_pdfs", output_dir="data/images", zoom=2):
    """
    Converts all PDF pages to images using PyMuPDF.
    zoom=2 means each page is rendered at 2× scale for better quality.
    """
    os.makedirs(output_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    for pdf_file in tqdm(pdf_files, desc="Converting PDFs → Images"):
        pdf_path = os.path.join(input_dir, pdf_file)
        doc = fitz.open(pdf_path)

        # For each page in the PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            matrix = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=matrix)
            output_path = os.path.join(
                output_dir,
                f"{os.path.splitext(pdf_file)[0]}_page{page_num + 1}.png"
            )
            pix.save(output_path)
        doc.close()

    print(f"Image conversion done! Files saved in: {output_dir}")

if __name__ == "__main__":
    convert_pdfs_to_images()

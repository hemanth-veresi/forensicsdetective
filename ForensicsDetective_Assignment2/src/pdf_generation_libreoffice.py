# pdf_generation_libreoffice.py
# ----------------------------------------------------
# Converts all .docx files to .pdf using LibreOffice
# Works well in GitHub Codespaces (Linux environment)

import os
import subprocess
from tqdm import tqdm

def convert_docx_to_pdf(input_dir="data/source_documents", output_dir="data/generated_pdfs"):
    os.makedirs(output_dir, exist_ok=True)

    files = [f for f in os.listdir(input_dir) if f.endswith(".docx")]

    for file in tqdm(files, desc="Converting DOCX → PDF"):
        input_path = os.path.join(input_dir, file)
        # LibreOffice command for headless conversion
        cmd = [
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"Conversion complete! PDFs saved in: {output_dir}")

if __name__ == "__main__":
    convert_docx_to_pdf()

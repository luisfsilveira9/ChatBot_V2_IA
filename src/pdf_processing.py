import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def save_extracted_text(pdf_path, output_dir):
    text = extract_text_from_pdf(pdf_path)
    base_name = os.path.basename(pdf_path).replace('.pdf', '.txt')
    output_path = os.path.join(output_dir, base_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return output_path

if __name__ == "__main__":
    pdf_directory = "../data/pdfs"
    output_directory = "../data/processed"
    os.makedirs(output_directory, exist_ok=True)

    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            save_extracted_text(pdf_path, output_directory)

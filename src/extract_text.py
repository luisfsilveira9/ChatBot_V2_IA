import fitz  # PyMuPDF

def extract_text_and_layout_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texts = []
    bboxs = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        texts.append(span["text"])
                        bboxs.append(span["bbox"])
    return texts, bboxs

if __name__ == "__main__":
    pdf_path = "../data/pdfs/sample.pdf"
    texts, bboxs = extract_text_and_layout_from_pdf(pdf_path)
    
    with open("../data/processed/sample_texts.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(texts))
    
    with open("../data/processed/sample_bboxs.txt", 'w', encoding='utf-8') as f:
        for bbox in bboxs:
            f.write(' '.join(map(str, bbox)) + '\n')

from flask import Flask, request, jsonify
from extract_text import load_model_and_tokenizer, extract_text_and_layout_from_pdf
import os

app = Flask(__name__)

model_path = "../models/layoutlm_model"
tokenizer, model = load_model_and_tokenizer(model_path)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    pdf_name = data.get('pdf_name')
    
    pdf_path = f"../data/pdfs/{pdf_name}.pdf"
    if not os.path.exists(pdf_path):
        return jsonify({"error": "PDF not found"}), 404

    texts, bboxs = extract_text_and_layout_from_pdf(pdf_path)
    
    # A função `answer_question` precisa ser ajustada para lidar com `texts` e `bboxs`
    answer = answer_question(question, texts, bboxs, model, tokenizer)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from extract_text import load_model_and_tokenizer, extract_text_and_layout_from_pdf
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

model_path = "../models/layoutlm_model"
tokenizer, model = load_model_and_tokenizer(model_path)

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/process', methods=['POST'])
def process():
    user_message = request.json['message']
    pdf_name = "sample"  # Nome do PDF processado
    pdf_path = f"../data/pdfs/{pdf_name}.pdf"
    
    if not os.path.exists(pdf_path):
        return jsonify({"error": "PDF not found"}), 404
    
    texts, bboxs = extract_text_and_layout_from_pdf(pdf_path)
    # A função `answer_question` precisa ser ajustada para lidar com `texts` e `bboxs`
    response = answer_question(user_message, texts, bboxs, model, tokenizer)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5003)

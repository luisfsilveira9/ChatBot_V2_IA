import os
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

def load_data_and_labels(filename):
    tokens, labels = [], []
    label_map = {'Magia': 0, 'Conflitos': 1, 'Personagens': 2, 'Outros': 3}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            token, label = line.strip().split('\t')
            tokens.append(token)
            labels.append(label_map[label])
    return tokens, labels
tokens, labels = load_data_and_labels('E:/Common Files/Lobsystem/ChatBot/labeled_tokens.txt')

# Inicializar o tokenizer BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

# Tokenizar os dados
inputs = tokenizer(tokens, return_tensors='tf', padding=True, truncation=True, max_length=512)

# Criar o dataset
def create_dataset(inputs, labels):
    dataset = tf.data.Dataset.from_tensor_slices(({
        'input_ids': inputs['input_ids'],
        'token_type_ids': inputs['token_type_ids'],
        'attention_mask': inputs['attention_mask']
    }, labels))
    dataset = dataset.batch(16)
    return dataset

dataset = create_dataset(inputs, labels)

# Configurar e treinar o modelo
model = TFBertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=4)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(dataset, epochs=1)

# Salvar o modelo após o treinamento
model_save_path = 'E:/Common Files/Lobsystem/ChatBot/models/my_chatbot_model'
os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
model.save(model_save_path)

import os
import torch
from transformers import LayoutLMTokenizer, LayoutLMForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

def load_data(file_path):
    texts = []
    labels = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            parts = line.strip().split('\t')
            if len(parts) == 2:
                text, label = parts
                texts.append(text)
                labels.append(int(label))
            else:
                print(f"Linha mal formada: {line.strip()}")
    return texts, labels

def main():
    model_path = "microsoft/layoutlm-base-uncased"
    tokenizer = LayoutLMTokenizer.from_pretrained(model_path)
    model = LayoutLMForSequenceClassification.from_pretrained(model_path, num_labels=5)  # Ajuste o número de labels conforme necessário

    texts, labels = load_data("../data/processed/texts_with_clusters.tsv")
    encodings = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

    dataset = Dataset.from_dict({
        'input_ids': encodings['input_ids'],
        'attention_mask': encodings['attention_mask'],
        'labels': torch.tensor(labels)
    })

    training_args = TrainingArguments(
        output_dir='../models/layoutlm_model',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    trainer.train()
    model.save_pretrained('../models/layoutlm_model')
    tokenizer.save_pretrained('../models/layoutlm_model')

if __name__ == "__main__":
    main()

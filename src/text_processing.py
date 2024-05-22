import os

def remove_suffix(word):
    suffixes = ['mente', 'ções', 'ção', 'amento', 'imento', 'adora', 'adores', 'ador', 'antes', 'ância', 'logia', 'logias']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def tokenize_and_process(content, stopwords):
    tokens = content.split()
    processed_tokens = [remove_suffix(token) for token in tokens if token.lower() not in stopwords]
    return processed_tokens

def save_processed_tokens(tokens, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for token in tokens:
            file.write(token + '\n')

def main():
    input_path = 'E:/Common Files/Lobsystem/ChatBot/texto_lei_processed.txt'
    output_path = 'E:/Common Files/Lobsystem/ChatBot/tokens_processed.txt'

    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    stopwords = set(["a", "e", "o", "é", "de", "do", "no", "são"])

    processed_tokens = tokenize_and_process(content, stopwords)

    save_processed_tokens(processed_tokens, output_path)

if __name__ == "__main__":
    main()

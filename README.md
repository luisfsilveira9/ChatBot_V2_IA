
# Projeto Chatbot - Processamento de Texto de Leis Municipais

Este projeto consiste em extrair, processar e utilizar texto das leis orgânicas municipais para treinar um modelo de machine learning. O objetivo é desenvolver um chatbot que possa responder perguntas relacionadas ao conteúdo dessas leis.

## Passos para Execução do Projeto

### Passo 1: Preparação do Arquivo PDF
- Coloque o arquivo PDF das leis orgânicas do município na pasta `C:/Users/SAMSUNG/Documents/ChatBot/`.
- O nome do arquivo deve ser claro, por exemplo: `lei_organica_municipio.pdf`.

### Passo 2: Extração do Texto do PDF
- Execute o script `extract_text.py`. Este script irá extrair o texto do PDF e salvá-lo em um arquivo `.txt`.
- Verifique se os caminhos dos arquivos estão corretos no script.

### Passo 3: Processamento Avançado do Texto
- Execute o script `text_processing.py`. Este script irá:
  - Carregar o texto do arquivo `.txt`.
  - Realizar tokenização, remoção de stopwords e stemming.
  - Salvar os tokens processados em outro arquivo `.txt` para uso posterior.

### Passo 4: Preparação e Treinamento do Modelo (Opcional)
- Prepare e treine seu modelo TensorFlow usando os tokens processados.
- Configure um modelo de Transformer ou outro modelo de NLP.
- Treine e valide o modelo com os dados processados.
- Salve o modelo treinado para uso futuro no sistema de chat.

### Passo 5: Integração com o Chatbot (Opcional)
- Integre o modelo treinado ao servidor do chatbot para que ele possa responder a perguntas sobre as leis com base nas interações dos usuários.

## Verificações Importantes
- Certifique-se de que todos os scripts estão na pasta `src/` e de que você tem permissões necessárias para ler e escrever nos diretórios especificados.
- Verifique se todas as dependências necessárias estão instaladas, incluindo `PyMuPDF` para `extract_text.py` e `nltk` para `text_processing.py`.

## Dependências
- Python 3.8+
- PyMuPDF
- NLTK
- TensorFlow

## Como Executar
- Abra um terminal.
- Navegue até a pasta do projeto.
- Execute os scripts na ordem descrita acima.

Este README oferece uma visão geral dos passos necessários para executar e desenvolver o chatbot baseado em leis municipais.

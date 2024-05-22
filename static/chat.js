async function sendQuestion() {
    const question = document.getElementById('question').value;
    const pdfName = "sample";  // Use o nome do PDF processado
    const response = await fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question, pdf_name: pdfName })
    });
    const data = await response.json();
    document.getElementById('chat-box').innerHTML += `<p><strong>Você:</strong> ${question}</p>`;
    document.getElementById('chat-box').innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
}

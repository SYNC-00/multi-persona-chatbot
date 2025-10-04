---
title: Multi-Persona Chatbot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.0
app_file: app.py
pinned: false
license: mit
---

# 🤖 Multi-Persona Chatbot

This project is an interactive **AI-powered chatbot** that can switch between different personalities:
- 🧠 **Psychologist** – offers kind and helpful advice.  
- 💻 **Coding Tutor** – teaches programming in a strict but supportive way.  
- 📖 **Storyteller** – creates fun and imaginative stories.  

### ✨ Features
- Switch between multiple personalities instantly.  
- Upload and read files (TXT, PDF, DOCX, CSV, JSON, Python code).  
- OCR support for images (JPG, PNG) to extract text.  
- Conversation history saved per personality.  

### 🚀 How to Use
1. Choose a personality from the dropdown.  
2. Type your message and click **Send** (or press Enter).  
3. Optionally, upload a file or image for the chatbot to read.  

### ⚙️ Tech Stack
- [Gradio](https://gradio.app/) for UI.  
- [OpenAI](https://openai.com/) for GPT responses.  
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDFs.  
- [python-docx](https://python-docx.readthedocs.io/) for Word documents.  
- [pytesseract](https://github.com/madmaze/pytesseract) for OCR.


## 🚀 Live Demo
👉 [Try the Chatbot Here](https://sync-x-multi-persona-chatbot.hf.space)

## 💻 Source Code
👉 [View on Hugging Face Repo](https://huggingface.co/spaces/Sync-x/multi-persona-chatbot)


## 📸 Screenshots

### Chatbot UI
![Chatbot UI](assets/chatbot-UI.png)

## Example Convo 1
![Chatbot Demo](assets/chatbot-demo1.png)

## Example Convo 2
![Chatbot Demo](assets/chatbot-demo2.png)


## ⚡ How to Run Locally
```bash
git clone https://huggingface.co/spaces/Sync-x/multi-persona-chatbot
cd multi-persona-chatbot
pip install -r requirements.txt
python app.py






---
---
title: Multi-Persona Chatbot
emoji: 📚
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.0
app_file: app.py
pinned: false
license: mit
short_description: Gradio powered AI Multi-Persona Chatbot
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


## 🚀 Live App
👉 [Try the Chatbot Here](https://sync-x-multi-persona-chatbot.hf.space)

## 💻 Source Code
👉 [View on Hugging Face Repo](https://huggingface.co/spaces/Sync-x/multi-persona-chatbot/tree/main)


## 📸 Screenshots

### Chatbot UI
![Chatbot UI](https://cdn-uploads.huggingface.co/production/uploads/68dff9c53bfa557fe78da574/2IZLY5FCGf301UKJwru2P.png)

## Example Convo 1
![Chatbot Demo](https://cdn-uploads.huggingface.co/production/uploads/68dff9c53bfa557fe78da574/POo_wL544GnLEjJcfgnFt.png)


## Example Convo 2
![Chatbot Demo](https://cdn-uploads.huggingface.co/production/uploads/68dff9c53bfa557fe78da574/hEGwFi7mRYtfcbPMSfNIP.png)


## ⚡ How to Run Locally
```bash
git clone https://huggingface.co/spaces/Sync-x/multi-persona-chatbot
cd multi-persona-chatbot
pip install -r requirements.txt
python app.py

---

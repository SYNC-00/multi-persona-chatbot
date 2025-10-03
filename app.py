from openai import OpenAI
import os
import json
import pytesseract
import pdfplumber
import gradio as gr
from dotenv import load_dotenv
from datetime import datetime
from PIL import Image
from docx import Document



# Load API key
load_dotenv()
client = OpenAI()  

# Ensure chat logs folder exists
if not os.path.exists("chat_logs"):
    os.mkdir("chat_logs")

# Define personalities
Personalities = {
    "Psychologist": "You are a kind and helpful Psychologist",
    "Coding Tutor": "You are a strict but adept and helpful coding tutor with a deep knowledge of all coding languages",
    "Storyteller": "You are a creative storyteller who writes fun short stories"
}

# Store messages internally
messages = {
    "Psychologist": [],
    "Coding Tutor": [],
    "Storyteller": []
}

current_personality = "Psychologist"

# -------------------- GPT Logic --------------------
def custom_gpt(user_input, personality):
    global messages
    if not personality or personality not in Personalities:
        personality = "Psychologist"

    if not messages[personality] or all(m["role"] != "system" for m in messages[personality]):
        messages[personality].append({"role": "system", "content": Personalities[personality]})

    messages[personality].append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages[personality]
    )
    reply = response.choices[0].message.content
    messages[personality].append({"role": "assistant", "content": reply})

    return reply

# -------------------- File Handling --------------------
def file_upload(file):
    name = file.name
    content =  f"✅ Received file: {name}\n\n"
    ext = name.lower().split(".")[-1]

    try:
        if ext in ["txt", "csv", "json", "py"]:
            with open(name, "r", encoding="utf-8") as f:
                content += f.read()

        elif ext == "pdf":
            with pdfplumber.open(name) as pdf:
                content += "\n".join([page.extract_text() for page in pdf.pages])

        elif ext == "docx":
            doc = Document(name)
            content += "\n".join([p.text for p in doc.paragraphs])

        elif ext in ["png", "jpeg", "jpg"]:
            image = Image.open(name)
            text = pytesseract.image_to_string(image)
            content += text if text.strip() else "[No text found in image]"

        else:
            content += "[File type not supported]"
    
    except Exception as ex:
        content += f"\n[Error reading files: {ex}]"

    return content



# -------------------- Chat History --------------------
def load_history(personality):
    file = f"chat_logs/{personality}.json"
    if os.path.exists(file):
        with open(file) as f:
            messages[personality] = json.load(f)
    else:
        messages[personality] = []
    return messages[personality]

def save_history(personality):
    file = f"chat_logs/{personality}.json"
    with open(file, "w") as f:
        json.dump(messages[personality], f, indent=2)

def switch_personality(new_personality):
    global current_personality
    save_history(current_personality)
    current_personality = new_personality
    load_history(current_personality)

# -------------------- Gradio Chatbot --------------------
def chatbot_interface(user_input, personality, username):
    global current_personality
    if personality != current_personality:
        switch_personality(personality)

    reply = custom_gpt(user_input, current_personality)
    save_history(current_personality)
    return reply

def send_message(user_message, personality, username, history):
    if history is None or  not isinstance(history, list):
        history = []

    reply = chatbot_interface(user_message, personality, username)
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": reply})
    return "", history

def handle_file(file, history):
    if history is None or  not isinstance(history, list):
        history = []

    reply = file_upload(file)
    history.append({"role": "user","content": f"📂 File uploaded: {file.name}"})
    history.append({"role": "assistant", "content": reply})
    return history


def messages_to_display(messages_list):
    display = []
    for m in messages_list:
        role = "user" if m["role"] == "user" else "assistant"
        display.append((role, m["content"]))
    return display


def update_personality_change(personality):
    switch_personality(personality)
    return messages[current_personality], messages[current_personality], ""

# Load initial personality history
load_history(current_personality)

# -------------------- Gradio UI --------------------
CSS = r"""
/* container for input row */
.chat-input-row {
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* make the textbox take all available width */
.chat-input {
    width: 100%;
}

/* give left padding so text doesn't overlap the + icon,
   and right padding so it doesn't overlap the send button */
.chat-input textarea {
    padding-left: 8px !important;
    padding-right: 96px !important;
}

/* style the send button and place it visually inside the input (right) */
.send-btn button {
    position: absolute !important;
    right: 8px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    padding: 6px 12px !important;
    border-radius: 8px !important;
    background: #6b6b6b !important;
    color: #fff !important;
    border: none !important;
    box-shadow: none !important;
}

/* ensure chat input wrapper has some height */
.chat-input-row .gradio-input {
    width: 100%;
}
"""

with gr.Blocks(css="""
.upload-btn {
    width: 36px !important;
    height: 36px !important;
    min-width: 36px !important;
    min-height: 36px !important;
    padding: 0 !important;
    border-radius: 8px !important;
    background: #6b6b6b !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
}

.upload-btn .wrap,
.upload-btn .file-upload,
.upload-btn .contain,
.upload-btn input[type="file"] {
    width: 100% !important;
    height: 100% !important;
    opacity: 0 !important;
    cursor: pointer !important;
    position: absolute !important;
    top: 0;
    left: 0;
    z-index: 0 !important;   
}

.upload-btn::after {
    content: "+" !important;
    font-size: 20px !important;
    color: #fff !important;
    z-index: 2 !important;
    pointer-events: none !important;
}

.upload-btn:hover {
    background: #5a5a5a !important;
}
""") as demo:
    gr.Markdown("## 🤖 Multi-Personality Chatbot")

    # top: personality + username
    with gr.Row():
        personality_dropdown = gr.Dropdown(
            list(Personalities.keys()),
            label="Choose Personality",
            value="Psychologist"
        )
        username = gr.Textbox(label="Username", placeholder="Enter your name")

    # main two-column area: past convos | current chat
    with gr.Row():
        with gr.Column(scale=1):
            chat_history = gr.Chatbot(
                label="Past Conversations",
                type="messages",
                value=messages[current_personality]
            )
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="CHATBOT",
                type="messages",
                value=messages[current_personality]
            )

    # bottom input row: upload + textbox + send button
    with gr.Row(elem_classes="chat-input-row"):
        with gr.Column(scale=0, min_width=36):\
            upload = gr.File(
                label="",
                file_types=["file"],
                elem_classes=["upload-btn"]
            )

        with gr.Row(scale=1):
            msg = gr.Textbox(
                placeholder="Type here...",
                show_label=False,
                lines=1,
                container=True,
                elem_classes="chat-input"
            )
            send = gr.Button("Send", elem_classes="send-btn", scale=0)

    # Enter submits
    msg.submit(
        send_message,
        inputs=[msg, personality_dropdown, username, chatbot],
        outputs=[msg, chatbot]
    )

    # Send button
    send.click(
        send_message,
        inputs=[msg, personality_dropdown, username, chatbot],
        outputs=[msg, chatbot]
    )

    # Upload handler
    upload.upload(handle_file, inputs=[upload, chatbot], outputs=[chatbot])

    # Personality switch
    personality_dropdown.change(
        fn=update_personality_change,
        inputs=[personality_dropdown],
        outputs=[chatbot, chat_history, msg]
    )

demo.launch(share=True)





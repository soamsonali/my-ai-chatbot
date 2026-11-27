# 🤖 AI Chatbot

A simple AI-powered chatbot built using **Python, Streamlit, and Groq API**. It provides an interactive chat interface where users can ask questions and receive AI-generated responses.

## ✨ Features

- Interactive chatbot interface using Streamlit.
- AI-generated responses powered by Groq.
- Chat history maintained during the active session.
- Clear Chat option to reset conversations.
- Custom dark-themed user interface.
- Secure API key management using environment variables.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Streamlit** – Frontend and web application framework.
- **Groq API** – AI model integration.
- **Llama/Groq-supported model** – Generates chatbot responses.
- **python-dotenv** – Loads environment variables securely.

## 📁 Project Structure

```text
chatbot/
│
├── chatbot.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

*Note: The `.env` file is kept locally and is not uploaded to GitHub.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Groq API key

Create a `.env` file in the project folder and add:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/keys).

### 7. Run the application

```bash
streamlit run chatbot.py
```

The chatbot will open in your browser.

## 🔄 How It Works

1. The user enters a question in the chat interface.
2. Streamlit captures the user's message.
3. Python sends the conversation history to the Groq API.
4. The AI model processes the input and generates a response.
5. The response is displayed in the chatbot interface.
6. Conversation messages are maintained using Streamlit session state.

## 🔐 Security

- API keys are stored in a local `.env` file.
- The `.env` file is excluded from GitHub using `.gitignore`.
- Never share or upload your private API key.

## 🚀 Future Improvements

- Add Retrieval-Augmented Generation (RAG).
- Enable document-based question answering.
- Add PDF and text document uploads.
- Maintain persistent chat history.
- Deploy the chatbot online.

## 👩‍💻 Author

**Sonali Singh**

GitHub: https://github.com/soamsonali

---

⭐ If you find this project interesting, feel free to explore the repository!

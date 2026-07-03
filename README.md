# 🎙️ Void GenAI - Advanced Voice-Controlled AI Assistant

<div align="center">
  <strong>An intelligent, highly extensible voice assistant powered by Python and Google's Gemini 2.0 Flash.</strong>
</div>
<br>

Void GenAI is a sophisticated voice-based digital assistant designed to execute system-level operations, browse the web, and answer complex queries using generative AI. It seamlessly integrates local OS capabilities with cloud-based Large Language Models to deliver an interactive and witty user experience.

---

## 🚀 Key Features

### 🧠 Generative AI Integration (Gemini 2.0 Flash)
Void GenAI leverages the `google-generativeai` SDK to process complex queries, provide explanations, and maintain conversational context. Additionally, the LLM is uniquely utilized to perform Natural Language Processing (NLP) tasks, such as extracting exact application executable names from unstructured user voice commands.

### 💻 System Automation & Control
- **Application Launching:** Uses a hybrid approach combining LLM-based entity extraction and Python's `subprocess` module to dynamically open local applications (e.g., VS Code, Photoshop, Chrome).
- **Automated Typing & Screenshots:** Utilizes `pyautogui` for hands-free text input and taking system-wide screenshots.
- **Platform Awareness:** Built-in OS checks (specifically optimized for Windows environments) to prevent execution errors on unsupported platforms.

### 🌐 Media & Web Integration
- **YouTube Automation:** Integrates `youtubesearchpython` to instantly scrape and play the top search result for any given query.
- **Broad Web Navigation:** Capable of instantly launching popular platforms including GitHub, Stack Overflow, LinkedIn, and more via the `webbrowser` module.
- **Information Retrieval:** Fetches and reads concise summaries directly from Wikipedia using the `wikipedia` library.

### 🎭 Sarcastic Persona & Edge-Case Handling
Unlike robotic assistants, Void features a pre-programmed witty and sarcastic persona, offering humorous greetings based on the time of day and snarky fallbacks when speech recognition times out or fails to parse audio.

---

## 🛠️ Architecture & Technical Stack

- **Language:** Python 3.x
- **Generative AI:** Google Gemini API (`gemini-2.0-flash`)
- **Speech Recognition:** `SpeechRecognition` (Google Web Speech API)
- **Text-to-Speech (TTS):** `pyttsx3` (Offline TTS engine)
- **Environment Management:** `python-dotenv` for secure API key injection.
- **System Interactions:** `os`, `subprocess`, `platform`, `pyautogui`

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **PyAudio** (Required by `SpeechRecognition` for microphone input. Installation may vary by OS).
- A valid **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/)).

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/render-TheVoid/void-GenAI.git
   cd void-GenAI
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   API_KEY=your_gemini_api_key_here
   ```

---

## 🕹️ Usage Guide

To start Void GenAI, simply run the main script from your terminal:

```bash
python void.py
```

### Example Voice Commands

Once the assistant greets you and begins listening, try the following commands:
- **General Queries:** *"Explain quantum computing"* or *"Who is Nikola Tesla?"*
- **Web Navigation:** *"Open GitHub"* or *"Open Stack Overflow"*
- **System Control:** *"Open VS Code"* or *"Take a screenshot"*
- **Media:** *"Play Interstellar soundtrack on YouTube"*
- **Utility:** *"What's the time?"* or *"Tell me a joke"*
- **Termination:** *"Stop"*

---

## 🧩 Project Structure

```text
void-GenAI/
├── void.py              # Main application script handling logic and routing
├── requirements.txt     # Python dependencies
├── .env                 # API keys and environment variables (Not tracked in git)
└── README.md            # Project documentation
```

---

## ⚠️ Known Limitations
- **OS Dependency:** Certain features like screenshotting, typing automation, and specific app launching are tightly coupled with the Windows OS environment.
- **Microphone Dependency:** Requires a functional microphone; background noise may affect speech recognition accuracy.

---

<div align="center">
  <i>Developed to bridge the gap between simple script automation and advanced LLM-powered interaction.</i>
</div>

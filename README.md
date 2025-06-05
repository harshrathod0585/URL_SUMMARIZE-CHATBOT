# 🚀 AI - Summarizer

This is an intelligent chatbot application that summarizes the content of any URL, including standard web pages and YouTube videos, using advanced language models and modern web scraping techniques. Built on [Streamlit](https://streamlit.io/) for an interactive chat interface, it delivers concise, context-preserving summaries, making it easy to digest long-form content quickly.

---

## ✨ Features

- **Summarize Any URL:** Paste a web page or YouTube link and get a well-structured summary.
- **YouTube Support:** Extracts and summarizes transcripts from YouTube videos, supporting multiple languages (en, gu, hi).
- **Custom Language Model:** Utilizes Groq's `gemma2-9b-it` model for high-quality, context-aware summarization.
- **Automatic Language Detection:** Summaries are generated in the detected language of the content.
- **Chunked Summarization:** Handles long content by splitting text into manageable chunks and merging their summaries.
- **Interactive Chat UI:** Built with Streamlit for a conversational experience.
- **Error Handling:** User-friendly error messages for invalid URLs or issues during processing.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- [Node.js](https://nodejs.org/) (for Playwright)
- [Playwright browsers](https://playwright.dev/python/docs/browsers) (installed automatically)

### Clone the Repository

```bash
git clone https://github.com/harshrathod0585/URL_SUMMARIZE-CHATBOT.git
cd URL_SUMMARIZE-CHATBOT
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Install System Dependencies

Some web scraping features require additional system libraries:

```bash
sudo apt-get update
sudo apt-get install $(cat packages.txt)
```

### Install Playwright Browsers

```bash
bash setup.sh
```

### Environment Variables

Create a `.env` file in the root directory and add your [Groq API key](https://groq.com/):

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Usage

Start the Streamlit app:

```bash
streamlit run app.py
```

- Open the local URL provided by Streamlit in your browser.
- Enter any web or YouTube URL in the chat input and get an instant summary!

---

## 🧩 How It Works

1. **Input Handling:** User pastes a URL in the chat interface.
2. **Validation:** The app checks if the URL is valid.
3. **Content Loading:**
   - For **web pages**: Uses Selenium and Playwright for robust scraping.
   - For **YouTube**: Extracts transcripts with `youtube_transcript_api`.
4. **Text Splitting:** Long documents are split into smaller chunks.
5. **Summarization:**
   - Each chunk is summarized independently.
   - All summaries are merged into a final, context-rich summary using Groq's LLM.
6. **Output:** The summary is displayed in the chat.

---

## 📝 Code Overview

- **app.py:** Main application logic, Streamlit UI, URL handling, summarization workflow.
- **requirements.txt / packages.txt:** Python and system dependencies.
- **setup.sh:** Script for installing Playwright browsers.

#### Key Libraries

- [Streamlit](https://streamlit.io/) for UI
- [LangChain](https://python.langchain.com/) for LLM orchestration
- [Groq](https://groq.com/) for LLM inference
- [Selenium](https://www.selenium.dev/) & [Playwright](https://playwright.dev/) for web scraping
- [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/) for YouTube support

---

## 💡 Example

> **User:** `https://en.wikipedia.org/wiki/Artificial_intelligence`  
> **NEXORA:** *(returns a 300–500 word summary of the Wikipedia article)*

---

## 🛡️ Troubleshooting

- **Playwright errors:** Ensure browsers are installed (`bash setup.sh`).
- **API key errors:** Check your `.env` file and Groq API key.
- **Missing system libraries:** Install dependencies listed in `packages.txt`.

---

## 🙏 Acknowledgements

- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq](https://groq.com/)
- [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/)

---

## 📫 Contact

For questions or feedback, open an issue or reach out to [harshrathod0585](https://github.com/harshrathod0585).

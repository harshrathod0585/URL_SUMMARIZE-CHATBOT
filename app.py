import validators,streamlit as st
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_core.documents import Document

import os 
from dotenv import load_dotenv
import subprocess
load_dotenv()

st.title("🚀 NEXORA - Summarizer")

def install_playwright_browsers():
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
    except Exception as e:
        st.warning(f"Warning: Playwright Chromium install failed: {e}")


install_playwright_browsers()


# st.sidebar.title("Configuration")
# api_key = st.sidebar.text_input("Enter Groq api key",type='password')
os.environ["PLAYWRIGHT_CHROMIUM_ARGS"] = st.secrets["PLAYWRIGHT_CHROMIUM_ARGS"]
api_key = st.secrets['GROQ_API_KEY']
if not api_key:
    st.error("Enter API key for continue")
    st.stop()

llm = ChatGroq(api_key=api_key,model="gemma2-9b-it",streaming=True)
map_template = """
You are a summarization expert. Summarize the following text efficiently while preserving its context and meaning.

Requirements:
- Limit the summary to 300 words.
- Ensure clarity and completeness.
- Write the summary in this language: {language}

Text:
{text}
"""
final_template = """
You are a summarization expert. Merge the following chunk summaries into one final, well-structured summary.

Requirements:
- Final summary should be within 500 words.
- Use bullet points, numbering, or subheadings where appropriate.
- Maintain context, avoid repetition, and ensure readability.
- Write the summary in this language: {language}

Chunk Summaries:
{text}
"""
map_prompt_template = PromptTemplate(input_variables=['text','language'],template=map_template)
final_prompt_template = PromptTemplate(input_variables=['text','language'],template=final_template)
with st.chat_message('ai'):
    st.write("Yo! Drop a valid URL and get a 🔥 summary — trust me, no one does it better 😎✨")

if url_prompt:= st.chat_input(placeholder="Paste Any Url For Summarizing"):
    
    if not validators.url(url_prompt) and not url_prompt.strip():
        st.error("Enter valid URL")
    else :
        with st.chat_message('user'):
            st.write(f"Summarize:{url_prompt}")
        with st.spinner("Loading..."):

            try:
                if "youtube.com" in url_prompt:
                    video_id = YoutubeLoader.extract_video_id(url_prompt)
                    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
                    matched_language = transcripts.find_transcript(['en','gu','hi'])
                    language = matched_language.language
                    transcript=matched_language.fetch().snippets
                    doc_text = " ".join([context.text for context in transcript])
                    data = [Document(page_content=doc_text,metadata={'source':'YouTube'})]
                else:
                    loader = SeleniumURLLoader(urls=[url_prompt])
                    data = loader.load()
                    language = "English"
                    
                final_data = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100).split_documents(data)
                chain = load_summarize_chain(
                    llm=llm,
                    chain_type='map_reduce',
                    map_prompt=map_prompt_template,
                    combine_prompt=final_prompt_template,
                )
                callback = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
                response = chain.run({"input_documents": final_data, "language": language},callbacks=[callback])
                with st.chat_message('ai'):
                    st.write(response)

            except Exception as e:
                st.error(f"Failed to summarize: {str(e)}")

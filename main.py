import os
import argparse
import sys
from summarizer import load_summarizer, summarize_text

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def run_streamlit_ui():
    import streamlit as st
    st.set_page_config(page_title="AI Notes Summarizer")
    st.title("🧠 AI Notes Summarizer")
    st.markdown("Summarize long notes and documents using AI (BART Model)")

    summarizer = load_summarizer()
    user_input = st.text_area("✍️ Paste your notes or paragraph here:", height=200)

    if st.button("🔍 Summarize"):
        if user_input.strip():
            summary = summarize_text(user_input, summarizer)
            st.subheader("📝 Summary:")
            st.success(summary)
        else:
            st.warning("Please enter some text to summarize.")

def main():
    parser = argparse.ArgumentParser(description="Summarize notes using BART")
    parser.add_argument('--file', type=str, help="Path to the text file")
    parser.add_argument('--ui', action='store_true', help="Launch Streamlit UI")
    args = parser.parse_args()

    if args.ui:
        run_streamlit_ui()
    elif args.file:
        text = read_file(args.file)
        summarizer = load_summarizer()
        summary = summarize_text(text, summarizer)
        print("\n🔍 Summary:\n", summary)
    else:
        print("⚠️ Please provide a file path using --file or use --ui to launch the web interface.")

if __name__ == "__main__":
    # If launched via `streamlit run main.py`, run the UI directly
    if "streamlit" in sys.argv[0]:
        run_streamlit_ui()
    else:
        main()

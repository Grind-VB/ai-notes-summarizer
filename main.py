import os
import argparse
from summarizer import load_summarizer, summarize_text

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Summarize notes using BART")
    parser.add_argument('--file', type=str, help="Path to the text file")
    parser.add_argument('--ui', action='store_true', help="Launch Streamlit UI")
    args = parser.parse_args()

    if args.ui:
        import streamlit as st
        st.title("🧠 AI Notes Summarizer")
        summarizer = load_summarizer()
        user_input = st.text_area("Paste your notes here:")
        if st.button("Summarize"):
            if user_input.strip():
                summary = summarize_text(user_input, summarizer)
                st.subheader("Summary:")
                st.write(summary)
    else:
        if not args.file:
            print("Please provide a file path using --file or use --ui for web interface.")
            return
        text = read_file(args.file)
        summarizer = load_summarizer()
        summary = summarize_text(text, summarizer)
        print("\n🔍 Summary:\n", summary)

if __name__ == "__main__":
    import sys
    if "streamlit" in sys.argv[0]:
        # Automatically launch UI when run via `streamlit run main.py`
        import streamlit as st
        st.title("🧠 AI Notes Summarizer")
        summarizer = load_summarizer()
        user_input = st.text_area("Paste your notes here:")
        if st.button("Summarize"):
            if user_input.strip():
                summary = summarize_text(user_input, summarizer)
                st.subheader("Summary:")
                st.write(summary)
    else:
        main()

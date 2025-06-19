from summarizer import load_summarizer, summarize_text
import streamlit as st

def run_streamlit_ui():
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

if __name__ == "__main__":
    run_streamlit_ui()

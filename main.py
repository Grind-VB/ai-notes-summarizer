from summarizer import load_summarizer, summarize_text
import streamlit as st

def run_streamlit_ui():
    st.set_page_config(
        page_title="AI Notes Summarizer",
        layout="wide",
        page_icon="🧠"
    )

    st.markdown("<h1 style='text-align: center;'>🧠 AI Notes Summarizer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Summarize long notes, articles, or paragraphs using the BART model</p>", unsafe_allow_html=True)
    st.markdown("---")

    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        length_option = st.selectbox(
            "Summary Length",
            ["Short", "Medium", "Long"]
        )
        if length_option == "Short":
            max_len, min_len = 60, 20
        elif length_option == "Medium":
            max_len, min_len = 130, 30
        else:
            max_len, min_len = 250, 50

        st.markdown("💡 Tip: Use *short* for notes, *medium* for articles, *long* for research papers.")

    # Load model with spinner
    with st.spinner("🔄 Loading summarization model..."):
        summarizer = load_summarizer()

    # Text input
    st.markdown("### ✍️ Paste your text below")
    user_input = st.text_area(
        "Text to summarize:",
        placeholder="Paste your notes or content here...",
        height=200,
        max_chars=3000
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"📝 **{len(user_input)} / 3000 characters**")

    with col2:
        if st.button("🔍 Summarize"):
            if user_input.strip():
                with st.spinner("⏳ Summarizing..."):
                    summary = summarize_text(user_input, summarizer, max_length=max_len, min_length=min_len)
                    st.success("✅ Summary generated!")
                    st.markdown("### 📝 Summary Output")
                    st.text_area("Summary:", value=summary, height=200)

                    # Download button
                    st.download_button("💾 Download Summary", summary, file_name="summary.txt")
            else:
                st.warning("⚠️ Please enter some text first.")

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>Made with ❤️ using BART by Hugging Face · Streamlit UI</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run_streamlit_ui()

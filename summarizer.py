from transformers import pipeline

def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")  # loads faster than bart-large-cnn

def summarize_text(text, summarizer, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

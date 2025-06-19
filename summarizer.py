from transformers import pipeline

def load_summarizer():
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return summarizer


def summarize_text(text, summarizer, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

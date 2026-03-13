from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()

    # Short summary: max 3 sentences
    num_sentences = min(3, len(text.split('.')))
    summary = summarizer(parser.document, num_sentences)

    summary_text = " ".join([str(sentence) for sentence in summary])
    return summary_text

import trafilatura
from newspaper import Article

def fetch_news(url):
    try:
        # Try Trafilatura first
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded)
            if text and len(text.strip()) > 200:
                return text

        # Fallback to Newspaper3k
        article = Article(url)
        article.download()
        article.parse()
        if article.text and len(article.text.strip()) > 200:
            return article.text

        # If both fail
        raise ValueError(
            "Unable to extract readable article text from this URL.\n"
            "Try a different news article."
        )

    except Exception as e:
        raise ValueError(f"Article extraction failed: {str(e)}")

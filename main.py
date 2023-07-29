import requests
import nltk
from bs4 import BeautifulSoup
from transformers import pipeline

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_website(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception if a HTTP error occurs
            return response.content
        except requests.exceptions.RequestException as e:
            print("Error: Failed to scrape the website")
            print(e)
            return ""

class TextProcessor:
    def __init__(self, content):
        self.content = content

    def preprocess_text(self):
        tokens = nltk.word_tokenize(self.content)
        pos_tags = nltk.pos_tag(tokens)
        named_entities = nltk.ne_chunk(pos_tags)
        return tokens, pos_tags, named_entities

class TextSummarizer:
    def __init__(self, content):
        self.content = content

    def summarize_text(self):
        try:
            summarization_model = pipeline("summarization")
            summary = summarization_model(self.content, max_length=100, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print("Error: Failed to summarize the text")
            print(e)
            return ""

def main():
    url = input("Enter the URL of the blog article: ")
    web_scraper = WebScraper(url)
    article_content = web_scraper.scrape_website()

    if article_content:
        text_processor = TextProcessor(article_content)
        tokens, pos_tags, named_entities = text_processor.preprocess_text()

        text_summarizer = TextSummarizer(article_content)
        summary = text_summarizer.summarize_text()

        print("\n------ Blog Article Summary ------\n")
        print(summary)
        print("\n----------------------------------\n")

if __name__ == "__main__":
    main()
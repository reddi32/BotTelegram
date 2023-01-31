import time
import requests
from bs4 import BeautifulSoup

def send_message(chat_id, text):
    # funzione per inviare un messaggio a Telegram
    url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_BOT_TOKEN)
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)

def check_for_new_article(site_url, article_title_selector):
    # funzione per verificare se ci sono nuovi articoli sul sito
    page = requests.get(site_url)
    soup = BeautifulSoup(page.content, "html.parser")
    article_title = soup.select_one(article_title_selector).text

    with open("notified_articles.txt", "a+") as f:
        f.seek(0)
        notified_articles = f.readlines()
        notified_articles = [x.strip() for x in notified_articles]

        if article_title not in notified_articles:
            send_message(TELEGRAM_CHAT_ID, "Nuovo articolo pubblicato: " + article_title)
            f.write(article_title + "\n")

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "163919711"
SITE_URL = "https://www.turismoroma.it/"
ARTICLE_TITLE_SELECTOR = "#latest-news h2 a"

check_for_new_article(SITE_URL, ARTICLE_TITLE_SELECTOR)

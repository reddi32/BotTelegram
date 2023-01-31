import time
import requests
from bs4 import BeautifulSoup

def send_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

def check_new_article(url, bot_token, chat_id):
    # Estrarre il contenuto del sito web
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = soup.find_all("article")
    # Verificare se ci sono nuovi articoli
    if len(articles) > 0:
        new_article = articles[0]
        title = new_article.find("h2").text
        # Inviare il messaggio su Telegram
        text = f"Nuovo articolo pubblicato: {title}"
        send_message(chat_id, text, bot_token)

# Impostare il URL del sito web
url = "https://www.turismoroma.it/"
# Sostituire con il token del bot
bot_token = "6165661441:AAGUdYk4oMsfuKV3hp5LDaeVZzB0VOnxdZQ"
# Sostituire con il chat ID
chat_id = "163919711"
# Verificare se ci sono nuovi articoli ogni 10 minuti
while True:
    check_new_article(url, bot_token, chat_id)
    time.sleep(600)

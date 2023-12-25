import time
import requests
from bs4 import BeautifulSoup

def send_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

def check_new_article(url, bot_token, chat_id, notified_articles):
    # Estrarre il contenuto del sito web
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = soup.find_all("article")
    # Verificare se ci sono nuovi articoli
    for article in articles:
        title = article.find("h2").text
        # Verificare se l'articolo è già stato notificato
        if title not in notified_articles:
            notified_articles.append(title)
            # Inviare il messaggio su Telegram
            text = f"Nuovo articolo pubblicato: {title}"
            send_message(chat_id, text, bot_token)
            # Aggiornare la lista degli articoli notificati
            with open("notified_articles.txt", "a", encoding='utf-8') as file:
                file.write(f"{title}\n")

# Caricare la lista degli articoli notificati
try:
    with open("notified_articles.txt", "r", encoding='utf-8') as file:
        notified_articles = file.read().splitlines()
except UnicodeDecodeError:
    # Se c'è un errore di decodifica, prova con un altro encoding
    with open("notified_articles.txt", "r", encoding='latin-1') as file:
        notified_articles = file.read().splitlines()
except FileNotFoundError:
    notified_articles = []

# Impostare il URL del sito web
url = "https://www.turismoroma.it/"
# Sostituire con il token del bot
bot_token = "6165661441:AAGUdYk4oMsfuKV3hp5LDaeVZzB0VOnxdZQ"
# Sostituire con il chat ID
chat_id = "163919711"

# Verificare se ci sono nuovi articoli ogni 10 minuti
while True:
    check_new_article(url, bot_token, chat_id, notified_articles)
    time.sleep(600)

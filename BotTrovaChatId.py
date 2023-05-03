import requests

# Sostituire con il token del bot
bot_token = "6033429575:AAGfE0qNaJ8e4vNyvCu7FPonAWq-5P-k1qI"

# Inviare una richiesta per ottenere gli aggiornamenti
response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")

# Parsare la risposta JSON
data = response.json()

# Trovare l'ID del chat
chat_id = data["result"][0]["message"]["chat"]["id"]

print(f"ID del chat: {chat_id}")

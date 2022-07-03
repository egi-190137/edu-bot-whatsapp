import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds  = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

contacts = client.open("chatbot_data").worksheet("contacts")
# quotes = client.open("chatbot_data").worksheet("quotes")
# messages = client.open("chatbot_data").worksheet("quotes")

list_guru = {
    'nama': contacts.col_values(1),
    'nomor': [ f'+{no}' for no in contacts.col_values(2) ]
}

# quotes = quotes.col_values(1)

# def getRandomQuote():
#     idx = random.randint(0, len(quotes) - 1)
#     return quotes[idx]
import gspread
from oauth2client.service_account import ServiceAccountCredentials

s = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds  = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",s)
client = gspread.authorize(creds)

sheet  = client.open("chatbot_reminders").sheet1

col_values = sheet.col_values(1)
row_filled = len(col_values)

    
def save_reminder_date(date):

    sheet.update_cell(row_filled+1, 1, date)
    print("saved date!")
    return 0

def save_reminder_time(time):

    sheet.update_cell(row_filled+1, 2, time)
    print("saved time!")
    return 0
    
def save_reminder_body(msg):

    sheet.update_cell(row_filled+1, 3, msg)
    print("saved reminder message!")
    return 0


from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

from dateutil.parser import parse
from validation_func import *
app = Flask(__name__)

list_guru = [
    "Pak Zainal",
    "Bu Ain",
    "Bu Sri",
    "Pak Abidin"
]

@app.route('/mybot', methods = ['POST'])

def mybot():
    incoming_msg = request.values.get('Body', '').lower()
    words = incoming_msg.split('@')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    # if 'hi' in incoming_msg:
    msg.body("Halo, Aku edu-bot\n\n"\
        "Ada yang bisa saya bantu?\n"\
        "- Buat quote\n"\
        "- Buat pengingat\n"\
        "- Tanya guru\n"\
        "- Buat pernyataan untuk guru")
    
    input_type = "command"
    responded = True

    if 'quote' in incoming_msg:
        r = requests.get('http://api.quotable.io/random')
        
        if r.status_code == 200:
            data  = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Sorry I am unable to retrieve quote at this time'
        
        msg.body(quote)
        responded = True

    if 'pengingat' in incoming_msg:
        reminder_string = "Masukkan tanggal sesuai format berikut.\n"\
        "dd/mm/yyyy"
        msg.body(reminder_string)

        input_type = "tanggal"
        responded = True

    if 'who are you' in incoming_msg:
        msg.body('Hi i am your bot')
        responded = True
    
    if "tanya guru" in incoming_msg:
        msg.body("Pilih salah satu guru berikut:\n"\
            "\n".join(list_guru)
        )
        responded = True

    if incoming_msg in list_guru:
        msg.body("Tulis pertanyaan anda dalam format berikut\n"\
            "*Tanya @* pertanyaan...")
        responded = True

    if input_type == "tanggal":
        # Cek apakah inputan sesuai dengan format
        # ????????
        # Cek apakah inputan sesuai dengan format
        
        # JIka sesuai jalankan kode berikut
        set_reminder_date(input_string)
        
        reply="Please enter the time in the following format only.\n\n"\
            "_23:10_"
        msg.body(reply)

        responded = True


    # elif len(words) > 1:
    #     input_type = words[0].strip().lower()
    #     input_string = words[1].strip()
    #     if input_type == "date":
    #         reply="Please enter the time in the following format only.\n\n"\
    #         "*time @* _23:10_"
    #         set_reminder_date(input_string)
    #         msg.body(reply)
    #         responded = True
        
    #     elif input_type == "time":
    #         reply="Please enter the reminder message in the following format only.\n\n"\
    #         "*Reminder @* _type the message_"
    #         set_reminder_time(input_string)
    #         msg.body(reply)
    #         responded = True

    #     elif input_type == "reminder":
    #         print("yuhu")
    #         reply="Your reminder is set!"
    #         set_reminder_body(input_string)
    #         msg.body(reply)
    #         responded = True
    
    if not responded:
        msg.body('Hi I can tell only about quote and my identity')
    
    return str(resp)

def set_reminder_date(msg):
    p = parse(msg)
    date = p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0

def set_reminder_time(msg):
    p = parse(msg)
    time = p.strftime('%d/%m/%Y')
    save_reminder_time(time)
    return 0

def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0

if __name__ == "__main__":
    app.run()
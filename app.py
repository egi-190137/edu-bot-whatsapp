import os

# from zmq import Message
from flask import Flask, request
# import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# from dateutil.parser import parse
# from validation_func import *
# from pandas import read_csv

from gsheet_func import list_guru
# from message_func import *
from get_message_info import *

app = Flask(__name__)

client = Client(
    os.environ['TWILIO_ACCOUNT_SID'],
    os.environ['TWILIO_AUTH_TOKEN']
)

@app.route('/mybot', methods = ['POST'])

def mybot():
    incoming_msg = request.form.get('Body')#.lower()

    resp = MessagingResponse()
    msg = resp.message()

    responded = False

    if incoming_msg is None:
        msg.body("error")

        responded = True
        
        return str(resp)

    incoming_msg = str(incoming_msg).lower() 
    words = incoming_msg.split()

    if 'hi' in incoming_msg:

        msg.body(
        f"""
        Halo, Aku edu-bot
        
        Ada yang bisa saya bantu:
        1. Chat guru
        2. Quote motivasi

        *Input :* */chat* atau */quote* 
        """
        )
        responded = True
    
    elif incoming_msg == '/chat':
        out_list_guru = ""
        for (idx, guru) in enumerate(list_guru['nama']):
            out_list_guru += f"{idx+1}. {guru}\n"
        
        msg.body(
        f"""
        Halo, Aku edu-bot
                
        Daftar guru:
        {out_list_guru}

        *Format :* Pilih [angka]
        """
        )
        responded = True

    elif 'pilih' == words[0]:
        if len(words) == 1:
            msg.body("Masukkan angka dengan benar!!!")
        elif words[1].isnumeric():      
            idx = int(words[1]) - 1

            if idx >= len(list_guru['nama']) and idx >= 0:
                msg.body("Pilihan anda tidak sesuai!!!")
            else:
                msg.body(
                    f"""
                    Masukkan nama anda:
                    
                    *Format :*
                    
                    nama [nama anda]"""
                )
                addData('idx', int(words[1]) - 1)

                
        else:
            msg.body("Masukkan angka dengan benar!!!")

        responded = True
    
    elif 'nama' == words[0]:
        if len(words) == 1:
            msg.body("Masukkan nama dengan benar!!!")
        else:
            msg.body(
                f"""
                Masukkan kelas anda :

                *Format :*
                Kelas [kelas anda]
                """
            )
            addData('nama', ' '.join(words[1:]).capitalize())
    
        responded = True
    
    elif 'kelas' == words[0]:
        if len(words) == 1:
            msg.body("Masukkan kelas dengan benar!!!")
        else:
            msg.body(
                f"""
                Masukkan pesan anda :

                *Format :*
                Pesan [pesan anda]
                """
            )

            addData('kelas', ' '.join(words[1:]).capitalize())
        
        responded = True

    elif 'pesan' == words[0]:
        if len(words) == 1:
            msg.body("Masukkan pesan dengan benar!!!")
        
        else:
            addData('pesan', ' '.join(words[1:]))

            message_info = getDictAllData()
            
            idx_no_tujuan = int(message_info['idx'][-1])
            message_body = f"""
            Dari\t: {message_info['nama'][-1]}
            Kelas\t: {message_info['kelas'][-1]}

            Pesan:
            {message_info['pesan'][-1]}
            """
            message = client.messages.create(
                body=message_body,
                from_='whatsapp:+14155238886',
                to=f'whatsapp:{list_guru["nomor"][idx_no_tujuan]}'
            )
            msg.body("Pesan berhasil terkirim")
        
        responded = True
    
    if not responded:
        msg.body('Perintah tidak dapat dikenali')
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
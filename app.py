import os
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from dateutil.parser import parse
from validation_func import *
from pandas import read_csv

from gsheet_func import *
from message_func import *

app = Flask(__name__)

df = read_csv('contacts.csv')

list_guru = df.to_dict('list')

client = Client(
    os.environ['TWILIO_ACCOUNT_SID'],
    os.environ['TWILIO_AUTH_TOKEN']
)

idx = None
name = ''
kelas = ''
message = ''


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
        out_list_guru = ""
        for (idx, guru) in enumerate(list_guru['nama']):
            out_list_guru += f"{idx+1}. {guru}\n"

        msg.body(
        f"""
        Halo, Aku edu-bot
        
        Daftar guru:
        {out_list_guru}

        Pilih salah satu guru dengan mengetikkan nama atau no pada pilihan
        """
        )
        responded = True
    
    elif 'pilih' in incoming_msg:
        if len(words) == 1:
            msg.body("Masukkan angka dengan benar!!!")
        elif words[1].isnumeric():      
            idx = int(words[1]) - 1
            
            if idx >= len(list_guru['nama']):
                msg.body("Pilihan anda tidak sesuai!!!")
            else:
                msg.body(
                    f"""
                    Masukkan nama anda:
                    
                    *Format :*
                    nama [nama anda]"""
                )
        else:
            msg.body("Masukkan angka dengan benar!!!")

        responded = True
    
    elif 'nama' in incoming_msg:
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
            name = " ".join(words[1:]).capitalize()
    
        responded = True
    
    elif 'kelas' in incoming_msg:
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

            kelas = words[1:]
        
        responded = True

    elif 'pesan' in incoming_msg:
        if len(words) == 1:
            msg.body("Masukkan pesan dengan benar!!!")
        
        else:
            message_body = f"""
            Dari\t: {name}
            Kelas\t: {kelas}

            Pesan:
            {message}
            """
            message = client.messages.create(
                body=message_body,
                from_='whatsapp:+14155238886',
                to=f'whatsapp:{list_guru["nomor"][idx]}'
            )
            msg.body("Pesan berhasil terkirim")
        
        responded = True

    # Code untuk membuat pengingat
    if 'pengingat' in incoming_msg:

        msg.body(
            "Masukkan tanggal!!\n\n"\
            "*Format :* \n"\
            "\"Tanggal dd/mm/yyyy\""
        )

        responded = True
        
    # if words[0] == "tanggal":
    #     # Cek apakah inputan sesuai dengan format
    #     # ????????
    #     # Cek apakah inputan sesuai dengan format
        
    #     set_reminder_date(words[1])
        
    #     msg.body(
    #         "Please enter the time in the following format only.\n\n"\
    #         "*Format :* \n"\
    #         "\"Jam 23:10\""
    #     )

    #     responded = True
    
    # if words[0] == "jam":
    #     set_reminder_time(words[1])
        
    #     msg.body(
    #         f"{words[1]}"\
    #         f"{incoming_msg}"\
    #         "Masukkan pesan pengingat.\n\n"\
    #         "*Format :*\n"\
    #         "\"Pesan [Pesan anda]\""
    #     )

    #     responded = True

    # if words[0] == "pesan":
    
    #     set_reminder_body(" ".join(words[1:]))
        
    #     msg.body(
    #         "Pengingat anda berhasil dibuat!"
    #     )
    #     responded = True
    
    # CODE untuk buat pernyataan
    if 'buat' and 'pesan' in words:
        msg.body(
            "Masukkan nama:"\
            "*Format :*"\
            "Nama [nama anda]"
        )
        responded = True
    
    if 'nama' in words:
        set_name(" ".join(words[1:]))
        msg.body(
            """Masukkan absen:
            
            *Format :*
            Absen [absen anda]"""
        )
        responded = True
    
    if 'absen' in words:
        set_absen(words[1])
        msg.body(
            """Masukkan kelas anda:
            
            *Format :*
            Kelas [kelas anda]"""
        )
        responded = True

    if 'kelas' in words:
        set_kelas(" ".join(words[1:]))
        msg.body(
            """Masukkan tujuan anda:
            
            *Format :*
            Tujuan [nama anda]"""
        )
        responded = True

    if 'tujuan' in words:
        set_tujuan(" ".join(words[1:]))
        msg.body(
            """Masukkan pertanyaan anda:
            
            *Format :*
            Tanya [nama anda]"""
        )
        responded = True

    if 'tanya' in words:
        set_pertanyaan(" ".join(words[1:]))
        msg.body(
            f"""Assalamu'alaikum Wr. Wb
            Saya {msg_info['nama']} absen {msg_info['absen']} dari kelas {msg_info['kelas']}. Saya ingin {msg_info['tujuan']}. {msg_info['pertanyaan']}.
            
            Terima Kasih sebelumnya pak"""
        )
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

# def set_reminder_date(msg):
#     p = parse(msg)
#     date = p.strftime('%d/%m/%Y')
#     save_reminder_date(date)
#     return 0

# def set_reminder_time(msg):
#     p = parse(msg)
#     time = p.strftime('%d/%m/%Y')
#     save_reminder_time(time)
#     return 0

# def set_reminder_body(msg):
#     save_reminder_body(msg)
#     return 0

if __name__ == "__main__":
    app.run(debug=True)
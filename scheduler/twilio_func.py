from twilio.rest import Client
 
client = Client(
    os.environ['TWILIO_ACCOUNT_SID'],
    os.environ['TWILIO_AUTH_TOKEN']
)

def send_rem(date,rem):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='*REMINDER* '+date+'\n'+rem,
        to='whatsapp:+917696076160'
    )
     
    print(message.sid)
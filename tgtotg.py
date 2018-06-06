from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import sys



print('\n\nScript em Python feito por Érico Netto')
print('Cliente do WORKANA: Thiago Pereira')
print('Data de criação: 04/06/2018\n\n\n')

print(sys.argv)
if not len(sys.argv)==2:
    print('\n>Parâmetros incorretos ou faltando, o arquivo não encontrado!')
    sys.exit()

envfile = sys.argv[1]

print('\n\nIncio do script!\n')
print('>Parâmetros passados: \n')
print(' Config file: ' + envfile +"\n")

load_dotenv(envfile)

# Use your own values here
api_id = os.getenv("APP_ID") 
api_hash = os.getenv("API_HASH") 
my_phone =os.getenv("MY_PHONE")
session_name =os.getenv("SESSION_NAME")
originChannels = os.getenv("ORIGIN_CHANNELS").split(",") #['Teste Erico 1', 'TesteErico2']
destinyChannel = os.getenv("DESTINY_CHANNEL") #'teste 3 admin'

print('>APP_ID: %s \n' % api_id)
print('>API_HASH: %s \n' % api_hash)
print('>MY_PHONE: %s \n' % my_phone)
print('>SESSION_NAME: %s \n' % session_name)
print('>ORIGIN_CHANNELS: %s \n' %  ":".join(originChannels))
print('>DESTINY_CHANNEL: %s \n' % destinyChannel)
############################################################
############################################################

client = TelegramClient(session_name, api_id, api_hash, update_workers=1, spawn_read_thread=False)

if client.connect():
    if not client.is_user_authorized():
        phone_number = my_phone
        client.send_code_request(phone_number)
        myself = client.sign_in(phone_number, input('Enter code: '))



@client.on(events.NewMessage)
def my_event_handler(event):
    if event.chat.title in originChannels:
        client.forward_messages(destinyChannel, event.message)

client.idle()


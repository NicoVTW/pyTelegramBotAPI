#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1364773949:AAHoR-4R_yAsvPPeYisVvTndc2BMfbTwb8c'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ti do il benvenuto alla registrazione per il gruppo "STREETCULTURE" 
Segui le prossime istruzioni per accedere.
Vuoi accedere come?
CLIENTE o VENDITORE.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if messagge.text=='CLIENTE':
    bot.reply_to(message, 'Stai per accedere al gruppo di compra-vendita streetwear STREETCULTURE, sarai un possibile acquirente, non potrai inviare alcun messaggio, per mantenere il gruppo libero per i prodotti in vendita, se fossi interessato ad acquistare o avere ulteriori informazioni riguardo i prodotti mostrati, dovrai solo rispondere al prodotto con un messaggio privato al venditore. Digita CONTINUA per proseguire.')


bot.polling()

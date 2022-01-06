from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from methods import xabar, start

updater=Updater(token="5094555922:AAGwjpH_i-dOq2up6qmWzQrd9EZr4Y-aNo0", use_context=True)

dispatcher=updater.dispatcher

start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,xabar)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
print("Ok, bot yahshi ishlayabti") 
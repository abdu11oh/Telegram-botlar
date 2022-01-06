from telegram.ext import  Updater, CommandHandler,MessageHandler,Filters
from methods import start, xabar

updater=Updater(token="5082436978:AAFpnjAJe5g73gU9Eurq2nxkMwnHYcXTQbg", use_context=True)

dispatcher=updater.dispatcher

start_handler=CommandHandler("start",start)

message_handler=MessageHandler(Filters.text,xabar)



dispatcher.add_handler(start_handler)   

dispatcher.add_handler(message_handler)

updater.start_polling()
print("bot ishladi")
from keyboards import  main_menu


def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Assalomu alaykum <em><b> {user.username}</b></em>"
            f"  Maktab kundaligi botiga hush kelibsiz !!!",parse_mode="HTML",reply_markup=main_menu)
    
def xabar(update, context):
    xabar=update.message.text
    if xabar=="Dushanba":
        context.bot.send_message(chat_id=update.effective_chat.id,text="Dushanbadagi kundaliklar:\n Inglis-tili \n Inglis-tili \n Informatika \n Ona-tili \n Biologiya", reply_markup=main_menu)
    elif xabar=="Seshanba":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Seshanbadagi kundaliklar:\n Inglis-tili \n Inglis-tili \n Rus-tili \n Geografiya \n Matematika", reply_markup=main_menu)
    elif xabar=="Chorshanba":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Chorshanbadagi kundaliklar:\n Ingliz-tili \n Ingliz-tili \n Ximiya \n Rus-tili",reply_markup=main_menu)
    elif  xabar=="Payshanba":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Payshanbadagi kundaliklar:\n Ingliz-tili \n Ingliz-tili",reply_markup=main_menu)
    elif xabar=="Juma":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Jumadagi kundaliklar:\n Ingliz-tili \n Ingliz-tili",reply_markup=main_menu)
    elif xabar=="Shanba":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Shanbadagi kundaliklar:\n Ingliz-tili \n Ingliz-tili",reply_markup=main_menu)
    elif xabar=="SinfRaxbar":
        context.bot.send_message(chat_id=update.effective_chat.id, text="SinfRaxbar: Alexandra Vladimirovna \n📲 aloqa: @GAlexandraV \n📞 tel:+9989*-***-**-**",reply_markup=main_menu)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Noma'lum xabar, etiborli bo'ling")
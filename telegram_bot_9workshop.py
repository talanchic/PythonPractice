from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token = '5454083652:AAHu06ExXgmcXRn0X3DmZ36rxiukvK_kDOg')
updater = Updater(token = '5454083652:AAHu06ExXgmcXRn0X3DmZ36rxiukvK_kDOg')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет. Я бот для фильтра 'абв', введите текст.")

def filter(update, context):
    text = update.message.text.split()
    list = []
    for element in text:
        if 'абв' not in element:
            list.append(element)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))

start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, filter)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()

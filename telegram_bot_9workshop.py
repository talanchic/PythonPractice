from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token = '')
updater = Updater(token = '')
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

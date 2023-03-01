import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a função que responde com "oi"
def oi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='oi')

# Cria um objeto Updater com o token do bot
updater = Updater(token='6168314162:AAHEVtTGBz7Fh-NJiLUDWktfHklFU1SHfoY', use_context=True)

# Registra a função oi como um manipulador de mensagem
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), oi))

# Inicia o bot
updater.start_polling()

# Mantém o bot em execução
updater.idle()

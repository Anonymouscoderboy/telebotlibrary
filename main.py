import telebot
from reply import replies  # Import the module containing predefined replies

# Token of your Telegram bot
TOKEN = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TOKEN)

# Handler for all incoming messages
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text.lower()
    reply_text = replies.get_reply(text)
    if reply_text:
        bot.reply_to(message, reply_text)

# Start the bot
bot.polling()

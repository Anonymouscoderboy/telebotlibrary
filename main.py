import telebot

# Replace with your bot token
bot_token = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(bot_token)

# Predefined replies
replies = {
    'hello': 'Hello there!',
    'how are you?': 'I am doing well, thank you!',
    'bye': 'Goodbye!'
}

# Handle '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! I am your bot.")

# Handle text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()
    if text in replies:
        bot.reply_to(message, replies[text])
    else:
        bot.reply_to(message, "Sorry, I don't understand.")

# Run the bot
bot.polling()

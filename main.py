import telebot
import reply  # Import the module containing predefined replies

# Token of your Telegram bot
TOKEN = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TOKEN)

# Predefined commands and their respective replies
commands = {
    '/start': reply.start_reply,
    '/help': reply.help_reply,
    '/info': reply.info_reply,
    '/status': reply.status_reply,
    # Add more commands and their replies here
}

# Handler for all commands
@bot.message_handler(commands=list(commands.keys()))
def handle_commands(message):
    command = message.text.lower()
    if command in commands:
        bot.reply_to(message, commands[command])

# Start the bot
bot.polling()

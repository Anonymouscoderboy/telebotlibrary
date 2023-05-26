import logging
import telebot

TOKEN = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'
CHAT_ID = '-1001832126466'
LOG_FILE = 'chat_log.txt'

bot = telebot.TeleBot(TOKEN)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Store chat data in a log file
def store_chat_data(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(f'[{message.chat.id}] [{message.from_user.username}]: {message.text}\n')

# Load stored replies from the log file
def load_stored_replies():
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        return file.readlines()

# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    store_chat_data(message)

    stored_replies = load_stored_replies()
    for reply in stored_replies:
        if reply.strip().lower() == message.text.strip().lower():
            bot.reply_to(message, reply)
            break

# Start the bot
bot.polling()

\import logging
from telegram import Update, Filters
from telegram.ext import Updater, CommandHandler, MessageHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Predefined questions and replies
replies = {
    'hi': 'Hello!',
    'hello': 'Hi there!',
    'tum kon ho': 'Main ek Telegram bot hoon.',
    'thumra name kya hai': 'Mera naam ChatBot hai.',
    'where are you from': 'I am from the virtual world.',
    'tum kha rhete ho': 'Main har jagah maujood hoon!'
}

# Additional questions and replies
additional_replies = {
    'how old are you': 'I am ageless.',
    'what is your purpose': 'My purpose is to assist and provide information.',
    'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
    # Add more questions and replies here
}

# Handle /start command
def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your bot.")

# Handle text messages
def handle_text(update: Update, context):
    text = update.message.text.lower()
    if text in replies:
        context.bot.send_message(chat_id=update.effective_chat.id, text=replies[text])
    elif text in additional_replies:
        context.bot.send_message(chat_id=update.effective_chat.id, text=additional_replies[text])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't understand.")

def main():
    # Set up the Telegram bot
    updater = Updater(token='6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc', use_context=True)
    dispatcher = updater.dispatcher

    # Add command handler for /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add message handler for text messages
    text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text)
    dispatcher.add_handler(text_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

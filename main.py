import logging
import telebot

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a TeleBot instance
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def store_chat_data(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # Store the chat data in your desired format (e.g., save to a file, database, etc.)
    # Custom code for storing the chat data goes here


@bot.message_handler(func=lambda message: True)
def get_stored_reply(message):
    chat_id = message.chat.id
    text = message.text

    # Retrieve the stored reply based on the incoming message
    # Custom code for retrieving the stored reply goes here

    # Reply to the message with the stored reply
    bot.reply_to(message, stored_reply)


def main():
    bot.polling()


if __name__ == '__main__':
    main()

import logging
import telebot

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a new TeleBot instance
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def store_chat_data(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # Check if the message is a reply to a previous message
    if message.reply_to_message:
        replied_message_id = message.reply_to_message.message_id
        replied_message = message.reply_to_message.text

        # Store the question, reply, and user information in a file
        with open("chat_data.txt", "a") as file:
            file.write(f"Chat ID: {chat_id}\n")
            file.write(f"User ID: {user_id}\n")
            file.write(f"Question: {replied_message}\n")
            file.write(f"Reply: {text}\n")
            file.write("--------\n")


def main():
    # Start the bot
    bot.polling()


if __name__ == '__main__':
    main()

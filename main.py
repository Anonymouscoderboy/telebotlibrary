from telegram.ext import Updater
import logging

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc"
CHAT_DATA_FILE = "chat_data.txt"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def store_chat_data(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    message = update.message.text

    # Check if the message is a reply to a previous message
    if update.message.reply_to_message:
        # Retrieve the ID of the message being replied to
        replied_message_id = update.message.reply_to_message.message_id

        # Retrieve the text of the replied message
        replied_message = update.message.reply_to_message.text

        # Store the question, reply, and user information in a file
        with open(CHAT_DATA_FILE, "a") as file:
            file.write(f"Chat ID: {chat_id}\n")
            file.write(f"User ID: {user_id}\n")
            file.write(f"Question: {replied_message}\n")
            file.write(f"Reply: {message}\n")
            file.write("--------------------\n")

        logger.info("Chat data stored successfully.")


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register the message handler to analyze and store chat data
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), store_chat_data))

    updater.start_polling()
    logger.info("Bot started polling...")
    updater.idle()


if __name__ == '__main__':
    main()

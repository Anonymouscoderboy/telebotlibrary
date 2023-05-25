import logging
from pymongo import MongoClient
import telebot

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc"
MONGO_URI = "mongodb+srv://abc:abcd@cluster0.dzijde4.mongodb.net/?retryWrites=true&w=majority"  # Update with your MongoDB connection URI
DATABASE_NAME = "abc"
COLLECTION_NAME = "AIdata"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a MongoDB client and connect to the database
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Create the telebot instance
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def store_chat_data(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # Check if the message is a reply to a previous message
    if message.reply_to_message:
        replied_message = message.reply_to_message.text

        # Store the question, reply, and user information in the MongoDB collection
        data = {
            "chat_id": chat_id,
            "user_id": user_id,
            "question": replied_message,
            "reply": text
        }
        collection.insert_one(data)


def main():
    bot.polling()


if __name__ == '__main__':
    main()

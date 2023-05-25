import logging
import random
import telebot
from pymongo import MongoClient

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

# Create a new TeleBot instance
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply_with_stored_reply(message):
    # Retrieve the stored reply based on the incoming message text
    query = {"question": message.text.lower()}
    stored_reply = collection.find_one(query)

    if stored_reply:
        # Reply with the stored reply
        reply_message = stored_reply["reply"]
        bot.reply_to(message, reply_message)
    else:
        bot.reply_to(message, "I'm sorry, I don't have a stored reply for that.")


def main():
    # Start the bot
    bot.polling()


if __name__ == '__main__':
    main()

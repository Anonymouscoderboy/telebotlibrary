import logging
import os
import pymongo
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'
MONGO_URI = 'mongodb+srv://abc:abcd@cluster0.dzijde4.mongodb.net/?retryWrites=true&w=majority'  # Update with your MongoDB connection URI
DATABASE_NAME = 'abc'
COLLECTION_NAME = 'AIdata'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


def store_chat_data(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    message_text = update.message.text

    data = {
        'chat_id': chat_id,
        'user_id': user_id,
        'message_text': message_text
    }

    collection.insert_one(data)


def get_stored_reply(message_text):
    stored_reply = collection.find_one({'message_text': message_text})
    if stored_reply:
        return stored_reply['reply']
    else:
        return None


def reply_to_message(update, context):
    message_text = update.message.text

    stored_reply = get_stored_reply(message_text)
    if stored_reply:
        update.message.reply_text(stored_reply)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the message handler to store chat data
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), store_chat_data))

    # Register the message handler to reply based on stored replies
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), reply_to_message))

    updater.start_polling()
    logger.info('Bot started polling...')

    updater.idle()


if __name__ == '__main__':
    main()

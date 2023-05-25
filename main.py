import logging
import random
import telebot

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a new TeleBot instance
bot = telebot.TeleBot(TOKEN)

# Load the stored chat data from the file
stored_data = []
with open("chat_data.txt", "r") as file:
    data = file.read().split("--------")
    stored_data = [entry.strip() for entry in data if entry.strip()]


@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply_with_saved_data(message):
    # Select a random entry from the stored data
    if stored_data:
        random_entry = random.choice(stored_data)
        bot.reply_to(message, random_entry)
    else:
        bot.reply_to(message, "Sorry, I don't have any saved data to reply with.")


def main():
    # Start the bot
    bot.polling()


if __name__ == '__main__':
    main()

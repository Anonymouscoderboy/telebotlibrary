import telebot

# Create an instance of the TeleBot class and pass your bot token
bot = telebot.TeleBot('6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc')


# Start command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Hello! I'm your Telegram bot.")


# Help command handler
@bot.message_handler(commands=['help'])
def help(message):
    help_message = '''
    Available commands:
    /start - Start the bot
    /help - Show help
    /ping - Ping the bot
    '''
    bot.send_message(chat_id=message.chat.id, text=help_message)


# Ping command handler
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(chat_id=message.chat.id, text="Pong!")


# Store questions and answers in a dictionary
question_answer_dict = {}


# Save the question and answer in the dictionary
def save_question_and_answer(question, answer):
    question_answer_dict[question.lower()] = answer


# Retrieve the last reply given by the bot for a question
def get_last_bot_reply():
    # For simplicity, we assume the last reply is the latest answer for the question
    if question_answer_dict:
        return list(question_answer_dict.values())[-1]
    return None


# Analyze the stored questions and answers and return the appropriate reply for the given question
def get_reply_for_question(question):
    return question_answer_dict.get(question.lower())


# Other message handler
@bot.message_handler(func=lambda message: True)
def process_message(message):
    # Get the chat ID and message text
    chat_id = message.chat.id
    text = message.text
    
    # Save the question and answer
    if text.endswith('?'):
        # Store the question and answer in the dictionary
        save_question_and_answer(text, get_last_bot_reply())

    # Check if the bot has a reply for the current question
    reply = get_reply_for_question(text)
    if reply:
        bot.send_message(chat_id=chat_id, text=reply)


# Start the bot
bot.polling()

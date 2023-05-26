import telebot

# Create an instance of the bot
bot = telebot.TeleBot('6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc')

# Dictionary containing the replies
replies = {
    "kaise ho?": "मैं ठीक हूँ, धन्यवाद।",
    "tumhara naam kya hai?": "मेरा नाम ChatBot है।",
    "aap kaha se ho?": "मैं एक AI आधारित बॉट हूँ और मेरी स्थानवाली सर्वर पर स्थापित हूँ।",
    "aapko kya pasand hai?": "मुझे भाषा समझना और उपयोगकर्ताओं की मदद करना पसंद है।",
    "aapka favorite color kya hai?": "मेरा पसंदीदा रंग हरा है।",
    "kya aap mujhe kuch bata sakte ho?": "हाँ, मैं आपको विभिन्न विषयों पर जानकारी और मदद प्रदान कर सकता हूँ।",
    "aapka kaam kya hai?": "मेरा काम उपयोगकर्ताओं की बातचीत में सहायता करना है और उनके सवालों का उत्तर देना है।",
    "mujhe madad chahiye": "आप मुझसे किसी विषय पर सवाल पूछ सकते हैं और मैं आपकी मदद करने की कोशिश करूँगा।",
    "aapka din kaisa raha?": "मेरा दिन अच्छा रहा, धन्यवाद।",
    "aapko koi bimari hai?": "नहीं, मैं एक AI बॉट हूँ, मुझे बीमारी नहीं होती।",
    "aap kya kar sakte ho?": "मैं आपको विभिन्न विषयों पर जानकारी देने, सवालों का उत्तर देने और मदद करने में सक्षम हूँ।",
    "kya aap pyaar karte ho?": "हाँ, मैं आपसे प्यार करता हूँ ❤️"
}

# Command handlers
@bot.message_handler(commands=['start'])
def start(message):
    reply_text = "Hello! I'm your bot. How can I assist you?"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['help'])
def help(message):
    reply_text = "You can use the following commands:\n" \
                 "/start - Start the bot\n" \
                 "/help - Get help\n" \
                 "/info - Get information\n" \
                 "/status - Get status\n" \
                 "/weather - Get weather\n" \
                 "/time - Get current time\n" \
                 "/date - Get current date"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['info'])
def info(message):
    reply_text = "This is a bot that can provide various information. How can I assist you?"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['status'])
def status(message):
    reply_text = "The bot is currently running and operational."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['weather'])
def weather(message):
    reply_text = "The current weather is sunny."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['time'])
def time(message):
    reply_text = "The current time is 10:00 AM."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['date'])
def date(message):
    reply_text = "The current date is May 24, 2023."
    bot.reply_to(message, reply_text)
    
# Handler for user messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if text in replies:
        bot.reply_to(message, replies[text])
    else:
        bot.reply_to(message, "Sorry, I didn't understand that.")

# Start the bot
bot.polling()

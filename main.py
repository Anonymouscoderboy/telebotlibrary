import logging
import telebot

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Predefined questions and replies
replies = {
    'hi': 'Hello!',
    'hello': 'Hi there!',
    'tum kon ho': 'Main ek Telegram bot hoon.',
    'thumra name kya hai': 'Mera naam ChatBot hai.',
    'where are you from': 'I am from the virtual world.',
    'tum kha rhete ho': 'Main har jagah maujood hoon!',
    'kaise ho?': 'मैं ठीक हूँ, धन्यवाद।',
    'tumhara naam kya hai?': 'मेरा नाम ChatBot है।',
    'aap kaha se ho?': 'मैं एक AI आधारित बॉट हूँ और मेरी स्थानवाली सर्वर पर स्थापित हूँ।',
    'aapko kya pasand hai?': 'मुझे भाषा समझना और उपयोगकर्ताओं की मदद करना पसंद है।',
    'aapka favorite color kya hai?': 'मेरा पसंदीदा रंग हरा है।',
    'kya aap mujhe kuch bata sakte ho?': 'हाँ, मैं आपको विभिन्न विषयों पर जानकारी और मदद प्रदान कर सकता हूँ।',
    'aapka kaam kya hai?': 'मेरा काम उपयोगकर्ताओं की बातचीत में सहायता करना है और उनके सवालों का उत्तर देना है।',
    'mujhe madad chahiye': 'आप मुझसे किसी विषय पर सवाल पूछ सकते हैं और मैं आपकी मदद करने की कोशिश करूँगा।',
    'aapka din kaisa raha?': 'मेरा दिन अच्छा रहा, धन्यवाद।',
    'aapko koi bimari hai?': 'नहीं, मैं एक AI बॉट हूँ, मुझे बीमारी नहीं होती।',
    'aap kya kar sakte ho?': 'मैं आपको विभिन्न विषयों पर जानकारी देने, सवालों का उत्तर देने और मदद करने में सक्षम हूँ।',
    'kya aap pyaar karte ho?': 'हाँ, मैं आपसे प्यार करता हूँ ❤️"
}

# Additional questions and replies
additional_replies = {
    'how old are you': 'I am ageless.',
    'what is your purpose': 'My purpose is to assist and provide information.',
    'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
    # Add more questions and replies here
}

# Initialize the bot
bot = telebot.TeleBot('6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc')

# Handle /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! I am your bot.')

# Handle text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()
    if text in replies:
        bot.reply_to(message, replies[text])
    elif text in additional_replies:
        bot.reply_to(message, additional_replies[text])
    else:
        bot.reply_to(message, "Sorry, I don't understand.")

# Start the bot
bot.polling()

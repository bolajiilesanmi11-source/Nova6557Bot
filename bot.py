import os
import telebot

# Get the token from environment variables (configured later on Render)
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

bot = telebot.TeleBot(BOT_TOKEN)

# This decorator listens for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Welcome to the Floearners Community 🎉"
    bot.reply_to(message, welcome_text)

# This keeps the bot running and listening for messages
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()

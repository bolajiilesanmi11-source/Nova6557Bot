import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging to see activity in Render logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # The welcome message you requested
    welcome_text = "💬 Join discussions, get updates, and connect with other"
    await update.message.reply_text(welcome_text)

if __name__ == '__main__':
    # Retrieve the token securely from Render environment variables
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        raise ValueError("Error: TELEGRAM_BOT_TOKEN environment variable is missing!")

    # Build the bot application
    # drop_pending_updates=True prevents the bot from spamming users if it restarts
    app = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    app.add_handler(CommandHandler("start", start))

    print("Bot is starting up... Polling for messages.")
    app.run_polling(drop_pending_updates=True)

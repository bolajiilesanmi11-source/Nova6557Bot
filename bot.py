import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging to force output directly to Render's log streams
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # The exact welcome message you requested
    welcome_text = "💬 Join discussions, get updates, and connect with other"
    await update.message.reply_text(welcome_text)

def main():
    # Fetch token
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("CRITICAL ERROR: TELEGRAM_BOT_TOKEN environment variable is missing!")
        sys.exit(1)

    logger.info("Initializing Telegram Bot...")
    
    # Build application
    app = ApplicationBuilder().token(TOKEN).build()

    # Register /start command
    app.add_handler(CommandHandler("start", start))

    logger.info("Bot is successfully running! Listening for Telegram messages...")
    
    # Start polling
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()

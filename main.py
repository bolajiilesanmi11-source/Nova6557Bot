import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging to help track errors in the Render dashboard
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the response to the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This captures the user's first name to personalize it
    user_name = update.effective_user.first_name
    
    welcome_text = (
        f"Hello {user_name}!\n\n"
        "Welcome to the Floearners Community 🎉"
    )
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_text
    )

if __name__ == '__main__':
    # Grab the token from Render's environment variables
    BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not BOT_TOKEN:
        raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables!")

    # Build the application
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Register the /start command handler
    application.add_handler(CommandHandler('start', start))
    
    # Run the bot via long polling
    print("Floearners Bot is starting up...")
    application.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from service import predict
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I am Cyberbullying Detection Bot.\nSend me a message, and I’ll classify it.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    result = predict(user_text)

    if result == "bullying":
        response = "⚠️ Bullying detected!"
        await update.message.reply_text(response)
        
    else:
       return
       #response = "✅ This message seems safe."
    

    

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

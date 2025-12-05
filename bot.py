from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv(8583344598:AAFdQPNfp-hXA2DWpr3ie0X01De8POIMJGo)

async def start(update, context):
    await update.message.reply_text("Бот запущен и работает!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

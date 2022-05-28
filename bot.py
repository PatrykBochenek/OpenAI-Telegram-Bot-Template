import constants as keys
from telegram.ext import *
import responses as resp

print("BOT STARTED...")

def start_command(update, context):
  update.message.reply_text("Ask me anything...")

def help_command(update, context):
  update.message.reply_text("Do you need help?")

def handle_message(update, context):
  text = str(update.message.text).lower()
  response = resp.ai_responses(text)

  update.message.reply_text(response)

def error(update, context):
  print(f"Update {update} cause error {context.error}")

def main():
  updater = Updater(keys.TELEGRAM_BOT_KEY, use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("start", help_command))

  dp.add_handler(MessageHandler(Filters.text, handle_message))

  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()

main()


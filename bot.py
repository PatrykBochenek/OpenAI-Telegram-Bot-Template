import constants as keys
from telegram.ext import *
import responses as R
import logger as lg

print("BOT STARTED...")

def start_command(update, context):
  update.message.reply_text("Bladee is my father...")
  ##lg.logUser(update)

def help_command(update, context):
  update.message.reply_text("u need help?")

def handle_message(update, context):
  text = str(update.message.text).lower()
  response = R.sample_responses(text)

  update.message.reply_text(response)

def error(update, context):
  print(f"Update {update} cause error {context.error}")

def main():
  updater = Updater('5312448921:AAG7BY4moCffb5um5KxzmPb2K4mbNYMet0Y', use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("start", help_command))

  dp.add_handler(MessageHandler(Filters.text, handle_message))

  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()

main()


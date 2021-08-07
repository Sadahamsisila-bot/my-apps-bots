
import constants as keys
from telegram.ext import
import Responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')



def help_command(update, context):
    update.message.reply_text('If you need help! You should ask for it on google!')

def handle_message(update, context):
    text = str(update.messege.text).lower()
    reponse = R.sample_responses(text)


    update.message.reply_text(reponse)


    def error(update, context):
        print(f"update {update} caused erroe {context.error}")


        def main():
            updater = update(keys.API_KEY,use_context=True )
            dp = update.dispatcher

            dp.add_handler(handle_message("start_command)"))
            dp.add_handler(handle_message("start_command)"))

            dp.add_handler(handle_message(filter.text, handle_message))

            dp.add_error_handler(error)

            updater.start_polling()
            updater.idle()


        main()

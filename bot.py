from telegram import Update , constants
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from functools import wraps


import APIkey
import openai



# Load your API key from an environment variable or secret management service
openai.api_key = APIkey.API_ChatGPT_Bot



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot create by Tamhv, please talk to me!")

async def ChatGPT(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = openai.Completion.create(model="text-davinci-003", prompt=update.message.text, temperature=0, max_tokens=4000)
    #print(response["choices"][0])
    #await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response["choices"][0]["text"])


if __name__ == '__main__':
    application = ApplicationBuilder().token(APIkey.API_Bot_Telegram_token).build()
    
    start_handler = CommandHandler('start', start)
    chatGpt_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), ChatGPT)



    application.add_handler(start_handler)
    application.add_handler(chatGpt_handler)


    application.run_polling()
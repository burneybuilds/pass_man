import json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


def read_json_data():
    
    with open("data.json", "r") as file:
        data = json.load(file)
        service = data["passwords"]
        print(service[0])
        print(service)
        for s in service:
            print(s["service"])


    # return data

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Hello! 👋 I am your PassMan bot."
#     )


def main():

    # TOKEN = 

    # app = Application.builder().token(TOKEN).build()

    # app.add_handler(
    #     CommandHandler("start", start)
    # )

    # print("Bot is running...")
    read_json_data()
    # app.run_polling()
    


if __name__ == "__main__":
    main()
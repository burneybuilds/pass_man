import json
from telegram import Update
from dotenv import load_dotenv
import os
from telegram.ext import Application, CommandHandler, ContextTypes

from handlers import send_request

def read_json_data():
    
    with open("data.json", "r") as file:
        data = json.load(file)

    return data

def get_password(search_request):
    data = []
    json_data = send_request(search_request)
    # data.append(json_data["service"])
    data.append(json_data["username"])
    data.append(json_data["password"])
    
    # for d in data:
    #     if d["service"] == search_request :
    #         return d["password"]
    
    return data

def add_new_data():
    ...

def list_of_services():
    json_data = read_json_data()
    data = json_data["passwords"]
    services = []

    for d in data:
        services.append(d["service"])

    return services


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! 👋 I am your PassMan bot."
    )

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    # check if the context.args is empty and showes a erroe message.
    if not context.args: 
        await update.message.reply_text(
                    "Please provide a service name. \n Example: /get Instagram"
        )
        return 
    
    search_request = context.args[0]
    
    password  = get_password(search_request)
    services_text = "\n".join(password)
    if password == None:
        await update.message.reply_text(
            f"{services_text}"
        )
    else:
       await update.message.reply_text(
            f"{services_text}"
        )

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    services = list_of_services()
    services_text = "\n".join(services)
    await update.message.reply_text(
        f"{services_text}"
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    search_request = context.args[0]

def main():
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )
    app.add_handler(
        CommandHandler("get", get)
    )
    app.add_handler(
        CommandHandler("list", list)
    )
    print("Bot is running...")
    
    app.run_polling()
    


if __name__ == "__main__":
    main()
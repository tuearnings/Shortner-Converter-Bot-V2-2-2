# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28052351"))
API_HASH = os.environ.get("API_HASH", "7255204a0099f982c9e60683eb50f288")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6229089991:AAEIg4SydZVURL5PzuQSn2edaCY2YjLNoME")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("
678272787")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "tulinks")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Kiran6412:160650913@cluster0.mq4z0hu.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "678272787")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001946243122")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tulinks_official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

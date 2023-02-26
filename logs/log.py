import logging

logging.basicConfig(
    filename="./logs/fbot.log", 
    level=logging.INFO, 
    encoding='utf-8', 
    filemode="w"
)
logger = logging.getLogger("BotanLog")
logger
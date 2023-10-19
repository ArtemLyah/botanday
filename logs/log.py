import logging

FORMAT = "[%(levelname)s] %(name)s | %(asctime)s\nmsg: %(message)s"

logger = logging.getLogger("BotanLog")
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('./logs/logs.out', 'w')
form = logging.Formatter(FORMAT)
fileHandler.setFormatter(form)
logger.addHandler(fileHandler)
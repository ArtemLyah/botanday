from .bot_filters import CommandBot
from dispatcher import dp

if __name__ == "filters":
    dp.filters_factory.bind(CommandBot)
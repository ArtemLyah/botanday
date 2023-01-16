from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", "Вивести список команд"),
            types.BotCommand("botan_reg", "Зареєструватися у <b>ботан дня<\b>"),
            types.BotCommand("botan", "Показати ботана дня"),
            types.BotCommand("botan_leave", "Покинути ботан дня"),
            types.BotCommand("botan_top", "Вивести топ розумників"),
            types.BotCommand("botan_me", "Показати мою статистику"),
        ]
    )
from pyrogram import filters
@bot.on_message(filters.command("start"))
def start_command(client, message):
    print("This is the /start command")


@bot.on_message(filters.command("help"))
def help_command(client, message):
    print("This is the /help command")


@bot.on_message(filters.chat("KayAspirerProject"))
def from_kayaspirerproject(client, message):
    print("New message in @KayAspirerProject")

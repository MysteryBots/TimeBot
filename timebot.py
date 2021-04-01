import logging
from pyrogram import Client, idle
from Config import Config


logging.basicConfig(
	level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
	":memory:",
	api_id=Config.API_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN,
	plugins=dict(root="TimeBot"),
)


# Run Bot
if __name__ == "__main__":
	app.start()  # Not using run as wanna print...
	uname = app.get_me().username
	print(f"@{uname} Started Successfully!")
	idle()
	app.stop()
	print("Bot stopped. Alvida!")
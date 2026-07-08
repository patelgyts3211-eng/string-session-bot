from datetime import datetime
import time

print("UTC:", datetime.utcnow())
print("Timestamp:", time.time())

import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import (
    ApiIdInvalid,
    ApiIdPublishedFlood,
    AccessTokenInvalid,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = Client(
    ":memory:",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)

if __name__ == "__main__":
    print("Starting the bot")

    try:
        app.start()

    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")

    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")

    me = app.get_me()
    print(f"@{me.username} is now running!")

    # ===== LOGGER GROUP TEST =====
    print("LOGGER_GROUP =", repr(env.LOGGER_GROUP))

    if env.LOGGER_GROUP:
        try:
            app.send_message(
                int(env.LOGGER_GROUP),
                "✅ Bot Started Successfully"
            )
            print("Logger group test successful.")
        except Exception as e:
            print("Logger Error:", type(e).__name__, e)
    else:
        print("LOGGER_GROUP not found.")

    idle()

    app.stop()
    print("Bot stopped. Alvida!")

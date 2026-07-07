from Data import Data
from pyrogram import Client, filters
from pyrogram.types import Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# ================= HELP =================
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=Data.HELP,
        reply_markup=Data.home_buttons  # ✅ FIXED
    )


# ================= ABOUT =================
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=Data.home_buttons  # ✅ FIXED
    )


# ================= REPO =================
@Client.on_message(filter("repo"))
async def repo(bot: Client, msg: Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=Data.REPO,
        disable_web_page_preview=True,
        reply_markup=Data.home_buttons  # ✅ FIXED
    )

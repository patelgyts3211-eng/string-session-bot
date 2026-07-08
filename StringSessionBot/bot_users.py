from pyrogram import Client, filters
from pyrogram.types import Message
from StringSessionBot.database import SESSION
from StringSessionBot.database.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if not msg.from_user:
        return

    try:
        user = SESSION.get(Users, int(msg.from_user.id))

        if user is None:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()

    except Exception as e:
        SESSION.rollback()
        print("Database Error:", e)


@Client.on_message(filters.user(7383472822) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs : {users}", quote=True)

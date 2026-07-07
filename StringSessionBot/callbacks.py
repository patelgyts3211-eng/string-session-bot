import traceback

from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from StringSessionBot.generate import generate_session


ERROR_MESSAGE = (
    "⚠️ ᴏᴏᴘs! ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀʀᴇᴅ!\n\n"
    "**ᴇʀʀᴏʀ**: {}\n\n"
    "ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ sᴜᴘᴘᴏʀᴛ."
)


@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):

    try:
        query = callback_query.data.lower()

        bot_info = await bot.get_me()
        mention = bot_info.mention

        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.id

        # ================= HOME =================
        if query == "home":
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(
                    callback_query.from_user.mention,
                    mention
                ),
                reply_markup=Data.buttons,
            )

        # ================= ABOUT =================
        elif query == "about":
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.ABOUT,
                disable_web_page_preview=True,
                reply_markup=Data.home_buttons,
            )

        # ================= HELP =================
        elif query == "help":
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="**ʜᴇʀᴇ ɪs ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ**\n\n" + Data.HELP,
                disable_web_page_preview=True,
                reply_markup=Data.home_buttons,
            )

        # ================= GENERATE =================
        elif query == "generate":
            await callback_query.message.reply(
                "ᴘʟᴇᴀsᴇ ᴄʜᴏᴏsᴇ ᴛʜᴇ ʟɪʙʀᴀʀʏ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🧑‍💻 ᴘʏʀᴏɢʀᴀᴍ",
                                callback_data="pyrogram"
                            ),
                            InlineKeyboardButton(
                                "ᴛᴇʟᴇᴛʜᴏɴ 🧑‍💻",
                                callback_data="telethon"
                            ),
                        ]
                    ]
                ),
            )

        # ================= SESSION GENERATION =================
        elif query in ["pyrogram", "telethon"]:
            await callback_query.answer("Generating session...")

            try:
                if query == "pyrogram":
                    await generate_session(bot, callback_query.message)
                else:
                    await generate_session(bot, callback_query.message, telethon=True)

            except Exception as e:
                print(traceback.format_exc())
                await callback_query.message.reply(
                    ERROR_MESSAGE.format(str(e))
                )

    except Exception as e:
        print(traceback.format_exc())
        try:
            await callback_query.message.reply(
                ERROR_MESSAGE.format(str(e))
            )
        except:
            pass

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Data:

    generate_single_button = [
        InlineKeyboardButton(
            "🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥",
            callback_data="generate"
        )
    ]

    home_buttons = InlineKeyboardMarkup(
        [
            generate_single_button,
            [InlineKeyboardButton("🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
        ]
    )

    generate_button = InlineKeyboardMarkup(
        [generate_single_button]
    )

    buttons = InlineKeyboardMarkup(
        [
            generate_single_button,
            [
                InlineKeyboardButton(
                    "✨ ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs ᴀɴᴅ sᴛᴀᴛᴜs ✨",
                    url="https://t.me/Developer_patel_zoneykruwatell"
                )
            ],
            [
                InlineKeyboardButton("🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ 🤔", callback_data="help"),
                InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about"),
            ],
            [
                InlineKeyboardButton(
                    "💌 ᴏᴛʜᴇʀ ʙᴏᴛs 💌",
                    url="https://t.me/Developer_Gaming"
                )
            ],
        ]
    )

    START = """
ʜᴇʏ {}
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
1) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ

sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.
"""

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/repo - ɢᴇᴛ ʀᴇᴘᴏ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴘʀᴏᴄᴇss
/restart - ʀᴇsᴛᴀʀᴛ ʙᴏᴛ
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ**

ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ
"""

    REPO = """
💥 ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ
"""

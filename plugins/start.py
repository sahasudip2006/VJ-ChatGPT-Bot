from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[ BOTS UPDATE](https://t.me/main_channel_bot_update)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝 𝙼𝚘𝚟𝚒𝚎 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Ott_Movie_Request_Group')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.meSUDIPSAHA06'),
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/main_channel_bot_update')
                    ]
                ]
            )
        )
  

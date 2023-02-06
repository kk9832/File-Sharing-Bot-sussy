#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>★彡 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href='https://t.me/amit_08bot'>【💚➣𝙰𝙼𝙸𝚃➣💚】</a>\n★彡 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : <code>𝙷𝙴𝚁𝙾𝙺𝚄</code>\n★彡 CHANNEL : <a href='https://t.me/Anime_pirates'>JOIN NOW💕 </a>\n★彡 ONGOINGS : @Ongoing_Animes_Hats\n★彡 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱\n★彡 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 : @Animeandmotivation</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

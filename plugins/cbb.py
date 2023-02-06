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
            text = f"<b>★彡 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href='tg://user?id={OWNER_ID}'>【💚➣𝙰𝙼𝙸𝚃➣💚】</a>\n★彡 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : <code>𝙷𝙴𝚁𝙾𝙺𝚄</code>\n★彡 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 : <a href='https://www.youtube.com/channel/UCnNoCpe6tVmSQwMUEq1vQrg'>𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴💕 </a>\n★彡 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴 : <a href='https://t.me/amit_08bot'>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>\n★彡 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱\n★彡 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 : @CLASSROOM_LECTURESS</b>",
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

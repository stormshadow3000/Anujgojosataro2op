from pyrogram import filters

from SaitamaRobot import (BOT_ID, DRAGONS, arq)
from SaitamaRobot import pbot as eren               
from SaitamaRobot.utils.errors import capture_err
from SaitamaRobot.utils.pluginhelp import edit_or_reply
from SaitamaRobot.utils.filter_groups import chatbot_group


active_chats_bot = []
active_chats_ubot = []


# Enabled | Disable Chatbot


@eren.on_message(filters.command("chatbot") & ~filters.edited)
@capture_err
async def chatbot_status(_, message):
    global active_chats_bot
    if len(message.command) != 2:
        return await message.reply_text("**Usage**\n/chatbot [ON|OFF]")
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id

    if status == "ON" or status == "on" or status == "On":
        if chat_id not in active_chats_bot:
            active_chats_bot.append(chat_id)
            text = (
                "Chatbot Enabled Reply To Any Message "
                + "Of Mine To Get A Reply"
            )
            return await message.reply_text(text)
        await message.reply_text("ChatBot Is Already Enabled.")

    elif status == "OFF" or status == "off" or status == "Off":
        if chat_id in active_chats_bot:
            active_chats_bot.remove(chat_id)
            return await message.reply_text("Chatbot Disabled!")
        await message.reply_text("ChatBot Is Already Disabled.")

    else:
        await message.reply_text("**Usage**\n/chatbot [ON|OFF]")


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


@eren.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded,
    group=chatbot_group,
)
@capture_err
async def chatbot_talk(_, message):
    if message.chat.id not in active_chats_bot:
        return
    if not message.reply_to_message:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    query = message.text
    await eren.send_chat_action(message.chat.id, "typing")
    response = await lunaQuery(
        query, message.from_user.id if message.from_user else 0
    )
    await eren.send_chat_action(message.chat.id, "cancel")
    await message.reply_text(response)

__mod__name = "ChatBot"
__help__ = """
• /chatbot [ON|OFF] To Enable Or Disable ChatBot In Your Chat.
"""

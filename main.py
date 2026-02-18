from aiogram import Bot, Dispatcher, executor, types
from bot.config import BOT_TOKEN, OWNER_ID
from bot.handlers import handle_message
from bot.database import users, groups

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(
            "➕ Add me to Group",
            url=f"https://t.me/{(await bot.me).username}?startgroup=true"
        )
    )
    await message.reply(
        "🤖 <b>Group Chat Bot</b>\n\n"
        "• Human-like replies\n"
        "• Emoji reactions\n"
        "• Hindi + English\n\n"
        "Use /help",
        reply_markup=kb,
        parse_mode="HTML"
    )

@dp.message_handler(commands=["ping"])
async def ping(message: types.Message):
    await message.reply("🏓 Pong")

@dp.message_handler(commands=["stats"])
async def stats(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return
    await message.reply(
        f"👥 Users: {users.count_documents({})}\n"
        f"👨‍👩‍👧 Groups: {groups.count_documents({})}"
    )

@dp.message_handler(commands=["broadcast"])
async def broadcast(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return
    text = message.get_args()
    if not text:
        return
    for u in users.find():
        try:
            await bot.send_message(u["_id"], text)
        except:
            pass

dp.register_message_handler(handle_message, content_types=types.ContentTypes.TEXT)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

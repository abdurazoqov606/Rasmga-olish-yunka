import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- SERVERNI ULASH (Render uchun) ---
from keep_alive import keep_alive
# -------------------------------------

# --- SOZLAMALAR ---
API_TOKEN = '8636129369:AAF44oJDyG_9mFzhdUIDCPd8N8ycDBLHu4Y'

# !!! ADMIN ID RAQAMINI SHU YERGA YOZING !!!
# Masalan: ADMIN_ID = 584930201
ADMIN_ID = 5578555263

# Saytingiz manzili
BASE_URL = 'https://abdurazoqov606.github.io/Yunka/'

# Reklama matni (Eski funksiya)
FOOTER_TEXT = (
    "\n\n📢 Bizning kanal: @abdurazoqov606"
    "\n👨‍💻 Bot yaratuvchisi: @abduroziqov_edits"
)

# Loglarni yoqish
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcherni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Foydalanuvchi ma'lumotlarini olish
    user_name = message.from_user.first_name
    user_last_name = message.from_user.last_name if message.from_user.last_name else ""
    user_id = message.from_user.id
    user_username = f"@{message.from_user.username}" if message.from_user.username else "Username yo'q"
    
    # --- 1-QISM: FOYDALANUVCHIGA JAVOB (Eski funksiya) ---
    personal_link = f"{BASE_URL}?id={user_id}"
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 BOOM (Linkga kirish)", url=personal_link)]
    ])
    
    text = (
        f"👋 Salom, {user_name}!\n\n"
        f"Mana sizning maxsus linkingiz: 👇\n"
        f"<code>{personal_link}</code>\n\n"
        f"Buni do'stlaringizga tashlang va BOOM! 💥\n"
        f"{FOOTER_TEXT}"
    )
    
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

    # --- 2-QISM: ADMINGA XABAR (Yangi funksiya) ---
    if ADMIN_ID != 0: # Agar Admin ID kiritilgan bo'lsa
        try:
            admin_text = (
                f"🔔 <b>Yangi foydalanuvchi START bosdi!</b>\n\n"
                f"👤 <b>Ism:</b> {user_name} {user_last_name}\n"
                f"🆔 <b>ID:</b> <code>{user_id}</code>\n"
                f"🌐 <b>Username:</b> {user_username}"
            )
            await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")
        except Exception as e:
            print(f"Adminga xabar yuborishda xatolik: {e}")

@dp.message()
async def echo_handler(message: types.Message):
    # Har qanday gap yozsa javob berish
    await message.answer(f"Bot ishlamoqda... {FOOTER_TEXT}")

# Botni ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    # --- RENDER UCHUN SERVERNI YOQISH ---
    keep_alive()
    # ------------------------------------
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")

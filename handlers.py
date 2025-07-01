from telethon import events, Button
from config import Config
from database import db
from utils import extract_post_id, download_post, cleanup
import instaloader
import os
import asyncio

# /start buyrug'i uchun xush kelibsiz xabari
async def handle_start(event):
    bot = await event.client.get_me()
    tugmalar = [
        [Button.inline("📚 Yordam", b"help"), Button.inline("ℹ️ Bot haqida", b"about")]
    ]
    await event.reply(
        f"""✨ **{bot.first_name} botiga xush kelibsiz!** ✨\n\nMen Instagramdagi ochiq postlarni yuklay olaman.\nYopiq postlar uchun /auth orqali tizimga kiring.""",
        buttons=tugmalar
    )

# /help buyrug'i uchun yordam xabari
async def handle_help(event):
    matn = """🛠 **Foydalanish bo'yicha qo'llanma** 🛠\n\n1. Instagram post havolasini yuboring\n2. Profil rasmi uchun: `/dp username`\n3. Yopiq postlar uchun /auth kerak"""

    if Config.has_insta_creds:
        matn += "\n\n🔑 Umumiy login mavjud"

    try:
        await event.edit(
            matn,
            buttons=Button.inline("🔙 Orqaga", b"home")
        )
    except:
        pass

# /about buyrug'i uchun bot haqida ma'lumot
async def handle_about(event):
    try:
        await event.edit(
            """🌐 **Bot haqida**\n\n• Instagram postlarini yuklaydi\n• Yopiq postlar uchun login imkoniyati\n• Hech qanday ma'lumot saqlanmaydi""",
            buttons=Button.inline("🔙 Orqaga", b"home")
        )
    except:
        pass

# /auth buyrug'i uchun foydalanuvchi login jarayoni
async def handle_auth(event):
    async with event.client.conversation(event.chat_id) as conv:
        await conv.send_message("""🔐 **Instagramga kirish**\n\n⚠️ Faqat yopiq postlar uchun kerak\n⚠️ Ikkinchi akkaunt tavsiya qilinadi\n\nDavom etish uchun `yes` deb yozing, bekor qilish uchun `no` deb yozing""")

        javob = await conv.get_response()
        if javob.text.lower() not in ['yes', 'y']:
            return await conv.send_message("🚫 Bekor qilindi")

        await conv.send_message("📧 Instagram foydalanuvchi nomini yuboring:")
        username_msg = await conv.get_response()

        await conv.send_message("🔑 Parolni yuboring:")
        password_msg = await conv.get_response()

        try:
            loader = instaloader.Instaloader()
            loader.login(username_msg.text.strip(), password_msg.text.strip())
            db.set_user_credentials(event.sender_id, username_msg.text, password_msg.text)
            await conv.send_message("✅ Kirish muvaffaqiyatli")
        except Exception:
            await conv.send_message("❌ Kirishda xatolik. Ma'lumotlarni tekshiring")

# /unauth buyrug'i uchun chiqish
async def handle_unauth(event):
    if db.delete_user_credentials(event.sender_id):
        await event.reply("🔓 Kirish ma'lumotlari olib tashlandi")
    else:
        await event.reply("ℹ️ Saqlangan ma'lumot topilmadi")

# /dp buyrug'i uchun profil rasmini yuklash
async def handle_profile_pic(event):
    args = event.pattern_match.group(1).split()
    if len(args) < 1:
        return await event.reply("❌ Format: /dp username")

    username = args[0].strip('@')
    try:
        instaloader.Instaloader(quiet=True).download_profile(username, profile_pic_only=True)

        for file in os.listdir(username.lower()):
            if file.endswith(".jpg"):
                await event.client.send_file(
                    event.chat_id,
                    file=f"{username.lower()}/{file}",
                    caption=f"📸 @{username}"
                )
                break

        await cleanup(username.lower())
    except Exception:
        await event.reply("❌ Yuklab olishda xatolik yuz berdi")

# Instagram post havolasi yuborilganda uni yuklash
async def handle_download(event):
    post_id = extract_post_id(event.text)
    if not post_id:
        return

    status = await event.reply("⏳ Yuklanmoqda...")

    try:
        username, password = db.get_user_credentials(event.sender_id)

        if not username and Config.has_insta_creds:
            username, password = Config.INSTA_USERNAME, Config.INSTA_PASSWORD

        photos, videos, caption = await download_post(post_id, username, password)

        media = photos + videos
        if not media:
            return await status.edit("❌ Mediya topilmadi")

        caption = f"{caption}" if caption else "via @"

        for m in media:
            if os.path.getsize(m) > 50 * 1024 * 1024:
                await event.client.send_message(
                    event.chat_id,
                    f"⚠️ Fayl {os.path.basename(m)} 50MB dan katta, yuborilmadi."
                )
                continue
            try:
                await event.client.send_file(event.chat_id, m, caption=caption)
                await asyncio.sleep(1)
            except Exception as e:
                await event.client.send_message(
                    event.chat_id,
                    f"❌ Xatolik ({os.path.basename(m)}): {str(e)}"
                )

        await status.delete()

    except Exception as e:
        await status.edit(f"❌ Xatolik: {str(e)}")
    finally:
        await cleanup(f"-{post_id}")

# Inline tugmalarga ishlovchi funksiyalar
async def handle_callback(event):
    data = event.data.decode()
    if data == "home":
        await handle_start(event)
    elif data == "help":
        await handle_help(event)
    elif data == "about":
        await handle_about(event)

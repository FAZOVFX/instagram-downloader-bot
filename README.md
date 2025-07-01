# 📥 Instagram Yuklab Olish Bot (Telegram uchun)

![Python Versiyasi](https://img.shields.io/badge/python-3.8%2B-blue)
![Litsenziya](https://img.shields.io/badge/license-MIT-green)
![Ishtirokchilar](https://img.shields.io/badge/contributors-1-lightgrey)

Instagram postlari, reels (video) va profil rasmlarini **Telegram orqali bevosita yuklab olish** imkonini beruvchi kuchli funksiyalarga ega Telegram boti. Python yordamida yaratilgan va Instaloader + Telethon texnologiyalarida ishlaydi.

👉 GitHub manzili: [https://github.com/FAZOVFX/instagram-downloader-bot](https://github.com/FAZOVFX/instagram-downloader-bot)

---

## ✨ Asosiy imkoniyatlar

- 📥 Instagram postlari va reels videolarini yuklab olish (video va rasm)
- 👤 Instagram profil rasmini va biografiyasini ko‘rish
- 📊 Admin panel: foydalanuvchilar statistikasi
- 📢 Barcha foydalanuvchilarga xabar yuborish (broadcast)
- 📄 Xatoliklar uchun log yuritish tizimi
- ⚡ Redis ma'lumotlar bazasi bilan integratsiya

---

## 🛠️ O‘rnatish

1. Repozitoriyani klonlang:
   ```bash
   git clone https://github.com/FAZOVFX/instagram-downloader-bot.git
   cd instagram-downloader-bot
   ```

2. Kerakli kutubxonalarni o‘rnating:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Sozlash

Loyihaning asosiy papkasida `.env` fayl yarating va quyidagilarni yozing:

```env
API_ID=telegram_api_id
API_HASH=telegram_api_hash
BOT_TOKEN=bot_token
AUTH_USER_ID=admin_id_raqamlari
REDIS_HOST=redis_host_manzili
REDIS_PORT=redis_port
REDIS_PASSWORD=redis_parol
```

---

## 📲 Foydalanish

1. Botni ishga tushiring:
   ```bash
   python3 -m main
   ```

2. Instagram linklarini botga yuboring:
   - Post: `https://www.instagram.com/p/abc123`
   - Reels: `https://www.instagram.com/reel/xyz456`
   - Profil: `https://www.instagram.com/username/`

---

## 🎮 Buyruqlar

| Buyruq      | Tavsifi                             | Kimga ochiq         |
|-------------|--------------------------------------|----------------------|
| `/start`    | Botni ishga tushirish               | Barcha foydalanuvchilar |
| `/users`    | Umumiy foydalanuvchilar soni        | Admin                |
| `/bcast`    | Barcha foydalanuvchilarga xabar     | Admin                |
| `/logs`     | Xatolik loglarini ko‘rish           | Admin                |

---

## 🗃️ Ma’lumotlar bazasi (Redis)

1. Quyidagi xizmatlardan birida Redis bazasini yarating:
   - [Redis Cloud](https://redis.com)
   - [Upstash](https://upstash.com)

2. Redis ma’lumotlaringizni `.env` faylga kiriting.

---

## 🌐 Muhit o‘zgaruvchilari

| O‘zgaruvchi      | Tavsifi                               | Misol                           |
|------------------|----------------------------------------|----------------------------------|
| `API_ID`         | Telegram API ID                        | 123456                           |
| `API_HASH`       | Telegram API Hash                      | abcdef12345                      |
| `BOT_TOKEN`      | Telegram bot tokeni                    | 123456:ABC-DEF1234               |
| `AUTH_USER_ID`   | Admin Telegram IDlari (bo‘sh joy bilan ajratilgan) | 12345 67890           |
| `REDIS_HOST`     | Redis server manzili                   | your-redis-host.redislabs.com    |
| `REDIS_PORT`     | Redis porti                            | 12345                            |
| `REDIS_PASSWORD` | Redis paroli                           | kuchli_parol                     |

---

## 📦 Talab qilinadigan kutubxonalar

```txt
telethon
instaloader
requests
redis
python-dotenv
```

---

## 📝 Log yuritish

Barcha faoliyatlar `log.txt` faylida saqlanadi. Adminlar `/logs` buyrug‘i orqali xatoliklar loglarini ko‘rishlari mumkin.

---

## ❤️ Qo‘llab-quvvatlash

Xatolik topdingizmi? **Issue** oching!  
Loyiha yoqdimi? ⭐ yulduzcha bosishni unutmang!

---

## 🔗 Loyiha manbasi

GitHub repozitoriyasi:  
👉 [FAZOVFX/instagram-downloader-bot](https://github.com/FAZOVFX/instagram-downloader-bot)

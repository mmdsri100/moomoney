from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن ربات و آیدی کانال
BOT_TOKEN = "7555177573:AAGop22DX3Quyka6NufVYDmq71ojF-xZ410"
CHANNEL_ID = "@M00M0NEY"

def create_signal(trade_type: str, entry_price: float) -> str:
    # محاسبات قیمت‌ها
    if trade_type.lower() == "buy":
        sl = entry_price - 0.0050
        tp1 = entry_price + 0.0050
        tp2 = entry_price + 0.0075
        tp3 = entry_price + 0.0100
        tp4 = entry_price + 0.0125
    else:
        sl = entry_price + 0.0050
        tp1 = entry_price - 0.0050
        tp2 = entry_price - 0.0075
        tp3 = entry_price - 0.0100
        tp4 = entry_price - 0.0125

    # ساخت متن پیام با فرمت و اموجی
    return f"""📢 <b>{trade_type.upper()} SIGNAL</b>

🎯 <b>ENTRY:</b> {entry_price:.4f}

❌ <b>STOP LOSS:</b> {sl:.4f}

✅ <b>TP1:</b> {tp1:.4f}  
🎯 <b>TP2:</b> {tp2:.4f}  
🥅 <b>TP3:</b> {tp3:.4f}  
🏁 <b>TP4:</b> {tp4:.4f}
"""

# فرمان /buy
async def buy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗️ لطفاً عدد ورود رو وارد کن، مثل:\n/buy 2345.67")
        return
    try:
        entry = float(context.args[0])
    except ValueError:
        await update.message.reply_text("❗️ عدد ورود نامعتبره.")
        return

    msg = create_signal("Buy", entry)
    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="HTML")
    await update.message.reply_text("✅ سیگنال خرید با موفقیت ارسال شد.")

# فرمان /sell
async def sell_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗️ لطفاً عدد ورود رو وارد کن، مثل:\n/sell 2345.67")
        return
    try:
        entry = float(context.args[0])
    except ValueError:
        await update.message.reply_text("❗️ عدد ورود نامعتبره.")
        return

    msg = create_signal("Sell", entry)
    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="HTML")
    await update.message.reply_text("✅ سیگنال فروش با موفقیت ارسال شد.")

# ساخت اپلیکیشن و اضافه کردن هندلرها
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("buy", buy_command))
app.add_handler(CommandHandler("sell", sell_command))

print("✅ Bot is running...")
app.run_polling()

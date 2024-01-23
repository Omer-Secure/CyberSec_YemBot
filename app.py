from reply import *
from level1 import *
from level2 import *
from flask import Flask, request

secret = 'ioufbvewgr2492yf2gh'
url = 'https://cybersec-yembot.onrender.com' + secret

bot.remove_webhook()
bot.set_webhook(url)
app = Flask(__name__)

@app.route('/'+secret, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

# -------------------- الأوامر --------------------
@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, "🛡 مرحبا بك " + msg.chat.first_name + ' ' + msg.chat.last_name + " في قناة الأمن السيبراني\n\nالقناة تحوي كل محاضرات تخصص الأمن السيبراني\n\n- ارسل كلمة [قائمه] لعرض كل المواد 👍\n- ارسل [اسم الماده] مباشرة 👍")

# -------------------- الردود --------------------
@bot.message_handler(func=lambda msg: True)
def reply_message(msg):
    reply_func(msg)

# -------------------- ازرار شفافه --------------------
@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    call_plan(call)
    call_level1(call)
    call_level2(call)

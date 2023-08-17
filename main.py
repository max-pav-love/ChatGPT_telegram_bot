import telebot
import openai
from settings import AI_API_KEY, TG_API_KEY

bot = telebot.TeleBot(TG_API_KEY, parse_mode=None)
openai.api_key = AI_API_KEY

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.chat.id,'⚙ Нейросеть думает...')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': message.text},
        ]
    )
    bot.send_message(message.chat.id, response['choices'][0]['message']['content'])

bot.polling(none_stop=True)
import telebot as TeleBot
from aiogram import types

bot= TeleBot.TeleBot('7484262558:AAGsbYouU5wCGd0y01fi0H34S_CL5lDe5-Y')
TO_CHAT_ID = '5418100197'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'Здравствуйте, {message.from_user.first_name}! ')
    bot.send_message(message.chat.id,'Вы можете прислать свою историю или случай сюда. Также фото или видео')

@bot.message_handler(content_types=['text'])
def all_messages(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Отправлено')

@bot.message_handler(content_types=types.ContentType.PHOTO)
def send_to_admin(message: types.Message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    #bot.send_photo(message.chat.id, photo=message.photo[-1].file_id)
    bot.send_message(message.chat.id, 'Отправлено фото')

@bot.message_handler(content_types=types.ContentType.VIDEO)
def send_to_admin(message: types.Message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Отправлено видео')


bot.polling(none_stop=True)

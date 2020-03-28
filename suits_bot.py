import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = 'ddde6581e21f174213125a60f3bb1b0941b20886e470e1e5cc720966abd13a24ab3fbd7784970d63035e6'

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Задать вопрос', color=VkKeyboardColor.DEFAULT)

start_msg = "Вводи вопрос, не стесняйся"

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":get_random_id()})

def write_msg_keyboard(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id(),
        "keyboard": keyboard.get_keyboard()})

vk = vk_api.VkApi(token=token)

longpool = VkLongPoll(vk)

def handle_message(event):
    text = event.text.lower()
    if "привет" in text or "начать" in text or "здравствуйте" in text:
        write_msg(event.user_id, start_msg)
    else:
        write_msg(event.user_id,"Сейчас поищу")
        # Основной цикл

for event in longpool.listen():
    # новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if(event.to_me):
            handle_message(event)
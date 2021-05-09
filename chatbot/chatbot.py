from random import randint
# TODO Импорт токена лучше сделать с обработкой ошибки
#  try:
#     from settings import tok
#  except ImportError:
#     settings = None  # Для того, чтобы убрать замечание среду разработки.
#     print('Для работы бота...')
#     exit()

from _my_bot_token import token
import vk_api
import vk_api.bot_longpoll

group_id = 204325991


class FerstBot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as bag:
                print(bag)


    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.object.text)
            # TODO При отправке сообщения вы сами генерируете random_id. В библиотеке для генерации идентификатора
            #  есть специальная функция vk_api.utils.get_random_id.
            #  Подробнее можете посмотреть в примерах библиотеки:
            #  https://github.com/python273/vk_api/blob/master/examples/messages_bot/user_messages_bot.py#L55
            self.api.messages.send(
                message=event.object.text + ' я пока тока эхоо',
                random_id=randint(1, 2 ** 20),
                peer_id=event.object.peer_id,
            )
        else:
            print('пока неумехи', event.type)


if __name__ == '__main__':
    bot = FerstBot(group_id, token)
    bot.run()

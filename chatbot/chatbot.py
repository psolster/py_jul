from random import randint
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
        # self.api = self.vk.get_api()

    def run(self):
        print('запустился ран')
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as bag:
                print(bag)

    def on_event(self, event):
        print(event)
        # if events.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
        #     print(event.type)
        #     self.api.message.send(
        #         message=action.object.text,
        #         random_id=random.randint(1, 2 ** 20),
        #         peer_id=action.object.peer_id,
        #     )
        # else:
        #     print('пока неумехи', action.type)


if __name__ == '__main__':
    bot = FerstBot(group_id, token)
    bot.run()

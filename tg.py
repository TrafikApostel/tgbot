from time import sleep

import telethon
from telethon import TelegramClient, events  # импортируем нужные модули телетона
from telethon.tl.functions.channels import JoinChannelRequest
while True:
    try:
        api_id = 5091455  # задаем апи нашего аккаунта в телеграмм
        api_hash = '2d8ada7ff69cfb42880cd16ef2ebd4bd'  # задаем хеш нашего аккаунта в телеграмм
        keys = open('keys.txt', encoding='utf-8').read().split('\n')
        client = TelegramClient('+79944390051', api_id, api_hash)  # собираем телеграм клиента
        groups_ = open('links.txt').read().split('\n')
        group_main = open('mainchat.txt').read()
        groups = []
        with client:
            try:
                pass
                #client.loop.run_until_complete(client(JoinChannelRequest(group_main)))
            except telethon.errors.rpcerrorlist.FloodWaitError as e:
                print(f'sleep {e.seconds} add in group')
                sleep(e.seconds)
                #client.loop.run_until_complete(client(JoinChannelRequest(group_main)))
            for group in groups_:
                try:
                    #client.loop.run_until_complete(client(JoinChannelRequest(group)))
                    pass
                except telethon.errors.rpcerrorlist.FloodWaitError as e:
                    print(f'sleep {e.seconds} add in group')
                    sleep(e.seconds)
                    #client.loop.run_until_complete(client(JoinChannelRequest(group)))
                try:
                    groups.append(client.loop.run_until_complete(client.get_entity(group)).id)
                    print(f'{group} ready')
                except:
                    pass
        print('start')
        @client.on(events.NewMessage)  # обработчик который запускаеться при получении нового сообщения
        async def my_event_handler(event):  # берем событие
            try:  # Проверка чатов
                if event.message.peer_id.channel_id in groups:
                    for key in keys:
                        if key in event.message.message.lower():
                            await client.forward_messages(await client.get_entity(group_main), event.message)
                            print('good')
                            break
            except Exception as e:  # Проверка групп и каналов
                print("Error! " + str(e))
        client.start()  # запускаем нашего клиента
        client.run_until_disconnected()  # назначаем ему бесконечный цикл выполнения
    except Exception as e:  # Проверка групп и каналов
        print("Error! " + str(e))
        sleep(10)

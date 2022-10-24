# -*- coding: utf-8 -*-
import datetime
from random import uniform
from time import sleep

import telethon
from telethon import TelegramClient, events  # импортируем нужные модули телетона
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Channel, ChatPhoto, ChatBannedRights
def start_main():
    group_m = Channel(id=1862585551, title='24/7', photo=ChatPhoto(photo_id=5375333978661306610, dc_id=2, has_video=False, stripped_thumb=b'\x01\x08\x08\xd0V\xb9\xfba\x0c\xa3\xc9\xech\xa2\x8a\x02\xf7?'), date=datetime.datetime(2022, 10, 22, 12, 46, 11, tzinfo=datetime.timezone.utc), creator=False, left=False, broadcast=False, verified=False, megagroup=True, restricted=False, signatures=False, min=False, scam=False, has_link=False, has_geo=False, slowmode_enabled=False, call_active=False, call_not_empty=False, fake=False, gigagroup=False, noforwards=False, join_to_send=False, join_request=False, access_hash=-6731483068947536451, username='vghgghhhj', restriction_reason=[], admin_rights=None, banned_rights=None, default_banned_rights=ChatBannedRights(until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc), view_messages=False, send_messages=False, send_media=False, send_stickers=False, send_gifs=False, send_games=False, send_inline=False, embed_links=False, send_polls=False, change_info=True, invite_users=False, pin_messages=True), participants_count=None)
    api_id = 5091455  # задаем апи нашего аккаунта в телеграмм
    api_hash = '2d8ada7ff69cfb42880cd16ef2ebd4bd'  # задаем хеш нашего аккаунта в телеграмм
    keys = ['инфограф',
    'дизайн карточки',
    'рич контент',
    'дизайнер',
    'ищу дизайнера',
    'графический дизайн']
    anti_keys = ['портфолио в лс','скидка','делаю за отзыв','делаю инфограф','резюме, портфолио','портфолио, резюме']
    msgs = []
    client = TelegramClient('+79859013501', api_id, api_hash)  # собираем телеграм клиента
    # groups_ = open('links.txt').read().split('\n')
    # group_main = open('mainchat.txt').read()
    groups = [1626008146, 1337059888, 1425875581, 1156193082, 1313032628, 1460940481, 1338357615, 1407181648, 1140500499, 1392456791, 1727823405, 1555595808, 1446796972, 1577144709, 1555595808, 1646368753, 1727823405, 1680664909, 1476588544, 1642147409]
    # with client:
    #     try:
    #         pass
    #         #client.loop.run_until_complete(client(JoinChannelRequest(group_main)))
    #     except telethon.errors.rpcerrorlist.FloodWaitError as e:
    #         print(f'sleep {e.seconds} add in group')
    #         sleep(e.seconds)
    #         #client.loop.run_until_complete(client(JoinChannelRequest(group_main)))
    #     for group in groups_:
    #         try:
    #             groups.append(client.loop.run_until_complete(client.get_entity(group)).id)
    #         except:
    #             pass
    #         #sleep(uniform(40,60))
    # print(groups)
    print('start')
    @client.on(events.NewMessage)  # обработчик который запускаеться при получении нового сообщения
    async def my_event_handler(event):  # берем событие
        try:
            if event.message.peer_id.channel_id in groups:
                for key in keys:
                    if key in event.message.message.lower():
                        for key_ in anti_keys:
                            if key_ in event.message.message.lower():
                                print(event.message.message)
                                print('--'*20)
                                event.message = ''
                        if [event.message.message,event.message.from_id.user_id] in msgs:
                            event.message = ''
                        await client.forward_messages(group_m, event.message)
                        msgs.append([event.message.message,event.message.from_id.user_id])
                        if len(msgs) >= 100:
                            msgs.clear()
                        break
        except Exception as e:
            print("Error! " + str(e))
            print(event.message)
    client.start()  # запускаем нашего клиента
    client.run_until_disconnected()  # назначаем ему бесконечный цикл выполнения
if __name__ == '__main__':
    start_main()

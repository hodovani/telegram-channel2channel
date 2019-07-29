from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 123456
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)

inputChatName = "inputsource"
outputChatName = "thesourceoutput"


@client.on(events.NewMessage(chats=inputChatName))
async def normal_handler(event):
    message = event.message.to_dict()['message']
    peer = await client.get_entity(outputChatName)
    await client.send_message(entity=peer, message=message)

client.start()
client.run_until_disconnected()

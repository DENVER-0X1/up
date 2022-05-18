from telethon import TelegramClient, events, Button
import logging
from telethon.tl.types import DocumentAttributeVideo
#client.send_file(..., )
logging.basicConfig(level=logging.INFO)
# api_id and api_hash from https://my.telegram.org/apps
api_id = '7693275'
api_hash = '663dc33a0788f583f4d9d7c9e49e5fe0'
BOT_TOKEN = '5131146214:AAGLw0kOFJAmqBz4denAjOzd--4ueLa8AXI'
client = TelegramClient('user', api_id, api_hash).start(bot_token =
    BOT_TOKEN)

# This message can contain any text, links, and emoji:

@client.on(events.NewMessage(pattern='/pop'))
async def handler(event):
    await event.reply("Hello" ,
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/anoninjector")],
                        #[Button.inline("Inline Button",data="example")]
                    ])
message = "Hello! Thank you for contacting me 👍\nI'll be back soon and reply to your message."
@client.on(events.NewMessage())
async def handler(event):
	sender = await event.get_input_sender()
	
  #file="11.png" is attached image, its optional parameter
	#await client.send_message(sender, message, file="11.jpg")
	await client.send_message(sender, message, file="https://file4.joporn.me/s4/upload_dbc9e79ec0ce540213cc658546dae562/12311/JOPORN_NET_12311_480p.mp4",attributes=(DocumentAttributeVideo(0, 0, 0),))

client.run_until_disconnected()
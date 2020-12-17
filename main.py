from telethon import TelegramClient, events
import settings
#---- LOGGING
import logging
logging.basicConfig(format = "[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
                   level = logging.WARNING)
#---- LOGGING

client = TelegramClient("listener", settings.API_ID, settings.API_HASH)
client.parse_mode = "md"

def main():
    client.start()
    print("Userbot on!")
    client.run_until_disconnected()

@client.on(events.NewMessage(chats = settings.INPUT))
async def forward(event):
    text_message = event.message
    if text_message.text.startswith("SELL") or text_message.text.startswith("BUY"):
        message = event.message.text.split()
        caption = f"{message[0]} {message[1]} @ {message[3]}\n{message[4]} {message[5]}\n{message[6]} {message[7]}"
        await event.reply(caption)
    elif text_message.text.startswith("SIGNAL:"):
        message = event.message.text.split()
        caption = f"{message[1]} {message[2]} @ {message[4]}\n{message[5]} {message[6]}\n{message[11]} {message[12]}"
        await event.reply(caption)
    elif text_message.text.startswith("**"):
        message = event.message.text.split()
        caption = f"{message[1]} {message[0].replace('**', '')} @ {message[3].replace('Price:', '')}\nSL: {message[4].replace('Stop:', '')}\nTP: {message[5].replace('TP:', '')}"
        await event.reply(caption)
    #if key in settings.IO:
    #   await client.send_message(settings.IO[key], message = event.text, file = message.media)
    #await client.send_message(settings.OUTPUT, message = caption, file = text_message.media)

if __name__ == "__main__":
    main()
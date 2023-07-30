import asyncio
import birthday
import discord
import datetime
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s: %(message)s')
logger = logging.getLogger('bot')

# Get environment variables
TOKEN = os.environ.get('RYAN_BOT_TOKEN')
if not TOKEN:
    raise ValueError('RYAN_BOT_TOKEN environment variable not set.')

# Variable to track the last date the birthday message was sent
last_birthday_sent_date = None

# Create a Discord client (bot)
intents = discord.Intents.default()
intents.members = True  # Required to access member information
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user.name}')
    logger.info('------')
    for guild in client.guilds:
        channel = guild.system_channel
        await run_tasks(channel)


@client.event
async def on_guild_join(guild):
    # Get the default channel of the guild (where the bot can send messages)
    channel = guild.system_channel

    # Check if the bot has permission to send messages in the default channel
    if channel and channel.permissions_for(guild.me).send_messages:
        intro_message = "Hi, I'm RyanBot, nice to meet you!"
        logger.info("Sending introductory message to server.")
        await channel.send(intro_message)
    else:
        logger.warning(f"Unable to send introductory message in server '{guild.name}'.")


async def run_tasks(channel):
    global last_birthday_sent_date
    while True:
        today = datetime.date.today()
        if birthday.is_birthday() and today != last_birthday_sent_date:
            last_birthday_sent_date = today
            # message = 'Happy Birthday Ann! 🎂🎂🎂\n https://media.giphy.com/media/feio2yIUMtdqWjRiaF/giphy.gif'
            logging.info("Sending Happy Birthday message to channel.")
            await birthday.send_birthday_embed(channel)

        # Introduce a delay of 60 seconds between iterations
        # to unblock Discord gateway's heartbeat.
        await asyncio.sleep(60)

# Run the bot
client.run(TOKEN)

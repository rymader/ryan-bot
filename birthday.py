import datetime
import discord


def is_birthday():
    # Get the current time in UTC
    now_utc = datetime.datetime.utcnow()

    # Check if it's July 29th
    if now_utc.month == 7 and now_utc.day == 29:
        # Check if it's 1 AM UTC
        if now_utc.hour >= 0 and now_utc.minute >= 26 and now_utc.second >= 0:
            return True

    return False


async def send_birthday_embed(channel):
    embed = discord.Embed(
        title="Happy Birthday Ann! 🎂🎂🎂",
        color=discord.Color.gold()
    )

    gif_url = " https://media.giphy.com/media/feio2yIUMtdqWjRiaF/giphy.gif"

    embed.set_image(url=gif_url)

    await channel.send(embed=embed)

import discord
import asyncio
import os
from discord.ext import tasks
from datetime import datetime, date

TOKEN = os.getenv("DISCORD_TOKEN")  # ide a bot tokenje
CHANNEL_ID = int(os.getenv("CHANNEL_ID")) # ide a csatorna ID
if not TOKEN:
    raise ValueError("DISCORD_TOKEN nincs beállítva")
if not CHANNEL_ID:
    raise ValueError("CHANNEL_ID nincs beállítva")
# céldátum
TARGET_DATE = date(2026, 4, 12)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@tasks.loop(hours=24)
async def countdown():
    today = date.today()
    remaining = (TARGET_DATE - today).days
    
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"⏳ {remaining} nap van hátra!")

@client.event
async def on_ready():
    print(f"Bejelentkezve mint {client.user}")
    countdown.start()

client.run(TOKEN)
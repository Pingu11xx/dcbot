import os
import discord
from datetime import date

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN nincs beállítva")
if not CHANNEL_ID:
    raise ValueError("CHANNEL_ID nincs beállítva")

CHANNEL_ID = int(CHANNEL_ID)

# céldátum
TARGET_DATE = date(2026, 4, 12)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bejelentkezve mint {client.user}")

    today = date.today()
    remaining = (TARGET_DATE - today).days

    try:
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(f"⏳ {remaining} nap van hátra! @everyone")
        print("Üzenet elküldve.")
    except Exception as e:
        print(f"Hiba történt: {e}")
    finally:
        await client.close()

client.run(TOKEN)
import discord
from discord.ext import commands
from discord import app_commands
import requests
import random
import giphy_client
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')
api_key = os.getenv('api_key')
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f'Synced commands!')
    except Exception as e:
        print(e)


@bot.tree.command(name='waifu', description='Sends a waifu pic or gif')
async def waifu(interaction: discord.interactions):
    try:
        url = "https://api.waifu.pics/many/sfw/waifu"

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        payload = {
            "exclude": []
        }

        response = requests.post(url, headers=headers, json=payload)

        data = response.json()

        urls = data["files"]

        randomimg = random.choice(urls)
        await interaction.response.send_message(f'{randomimg}')
    except:
        api_instance = giphy_client.DefaultApi()
        api_response = api_instance.gifs_search_get(api_key, 'waifu', limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)
        await interaction.response.send_message(f"https://media.giphy.com/media/{giff.id}/giphy.gif")

#not even gonna test it bro ;-;
@bot.tree.command(name='nsfwwaifu', description='Sends a NSFW waifu pic or gif')
async def waifu(interaction: discord.interactions):
    url = "https://api.waifu.pics/many/nsfw/waifu"

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    payload = {
       "exclude": []
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    urls = data["files"]

    randomimg = random.choice(urls)
    await interaction.response.send_message(f'{randomimg}')
#start
bot.run(token)
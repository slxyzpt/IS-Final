import discord 
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
import json
import wikipedia
import requests
from bs4 import BeautifulSoup



def get_server_prefix(client, message):
    with open("BOT DISCORD/prefixes.json", "r") as f:
        prefix = json.load(f)
        
    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all())

bot_status = cycle(["หน้ามึงอยู่", "กับใจ", "กับความรู้สึก"])
@tasks.loop(seconds=5)
async def change_staus():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Success: Bot is connect to Discord")
    change_staus.start()
    
@client.event
async def on_guild_join(guild):
    with open("BOT DISCORD/prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(guild.id)] = "/"
    
    with open("BOT DISCORD/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open("BOT DISCORD/prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix.pop(str(guild.id))
    
    with open("BOT DISCORD/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
@client.command()
async def ตั้งค่า(ctx, *, newprefix: str):
    with open("BOT DISCORD/prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(ctx.guild.id)] = newprefix
    
    with open("BOT DISCORD/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
async def load():
    for filename in os.listdir("BOT DISCORD/cogs"):
        if filename.endswith(".py"):
           await client.load_extension(f"cogs.{filename[:-3]}")
           
@client.hybrid_command(name="หา",description="หาข้อมูลจากวิกิพีเดีย")
async def หา( ctx, *, query):
        try:
            wikipedia.set_lang('th')
            page = wikipedia.page(query)
            title = page.title
            summary = page.summary.split('\n')[0]

            embed1 = discord.Embed(title=title, description=summary, url=page.url,color=0x00ff00)
            await ctx.send(embed=embed1)
            
        except wikipedia.exceptions.DisambiguationError as e:
            options = '\n'.join(e.options)
            await ctx.send(f"Multiple results found. Please be more specific. Options:\n{options}")
            
        except wikipedia.exceptions.PageError:
            await ctx.send("Sorry, no page was found.")
              
            
@client.hybrid_command(name="ลิงก์",description="หาเวปไซต์จากคีย์เวิร์ด")
async def ลิงก์( ctx, *, query):
        url = 'https://www.google.com/search?q=' + query
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('a')
        links = []
        for r in results:
            link = r.get('href')
            if link.startswith('/url?q='):
                link = link[7:]
                if '&' in link:
                    link = link[:link.index('&')]
                links.append(link)
                if len(links) == 5:
                    break
        
        embed = discord.Embed(title=f"Search Results for '{query}'", color=discord.Color.blurple())
        for i, link in enumerate(links):
            embed.add_field(name=f"Result {i+1}", value=f"[{link}]({link})", inline=False)
        
        if not links:
            embed.description = "No search results found."
        
        await ctx.send(embed=embed)
        
async def main():
    async with client:
        await load()
        await client.start("")

asyncio.run(main())
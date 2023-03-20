import discord
from discord.ext import commands 
from discord import app_commands
import requests
from bs4 import BeautifulSoup
import random

class KRIT(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print("พร้อมเรื้อน ")
    
    @app_commands.command(name="กิต",description="ทักทาย")
    async def กิต(self, interaction: discord.Interaction):
        await interaction.response.send_message("เรื้อน")
        
    @app_commands.command(name="สัญญาณ",description="หาค่าความล่าช้า")
    async def สัญญาณ(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message({bot_latency})
        
    @app_commands.command(name="ข้าว",description="สุ่มรายการอาหาร")
    async def ข้าว(self,interaction: discord.Interaction ):
        with open("BOT DISCORD/cogs/responses.txt", encoding="utf8") as f:
          random_responses = f.readlines()
          response = random.choice(random_responses).strip()

        await interaction.response.send_message(response)
        
    @app_commands.command(name="ผู้ใช้", description="ดูโปรไฟล์ผู้ใช้")
    async def ผู้ใช้(self, interaction: discord.Interaction ,member: discord.Member=None):
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member
        
        info_embed=discord.Embed(title=f"ข้อมูลของ {member.name}", description="รายละเอียดข้อมูลผู้ใช้ทั้งหมด", color=member.color)
        info_embed.set_thumbnail(url=member.avatar)
        info_embed.add_field(name="ชื่อ:", value=member.name, inline=False)
        info_embed.add_field(name="ชื่อเล่น:", value=member.display_name, inline=False)
        info_embed.add_field(name="แท็ก:", value=member.discriminator,inline=False)
        info_embed.add_field(name="ID:", value=member.id, inline=False)
        info_embed.add_field(name="ยศ:", value=member.top_role,inline=False)
        info_embed.add_field(name="สถานะ:", value=member.status,inline=False)
        info_embed.add_field(name="วันที่สร้าง:", value=member.created_at.__format__("%A, %d. %B %Y @ %H:%M:%S"),inline= False)
                         
        await interaction.response.send_message(embed=info_embed)
        
async def setup(client):
    await client.add_cog(KRIT(client))

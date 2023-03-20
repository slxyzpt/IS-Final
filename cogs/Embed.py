import discord
from discord.ext import commands
from discord import app_commands

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="ที่มา", description="ที่มาของIS")
    async def ที่มา(self, interaction:discord.Interaction):
        Embed_IS= discord.Embed(title="IS", description="สรุป IS แบบย่อๆ")
        Embed_IS.set_author(name="Krxt")
        
        await interaction.response.send_message(embed=Embed_IS)
    
    @app_commands.command(name="คำสั่ง", description="คำสั่งทั้งหมด")
    async def คำสั่ง(self, interaction: discord.Interaction):
        Embed_help = discord.Embed(title="ชุดคำสั่ง", description="คำสั่งทั้งหมด")
        Embed_help.set_author(name="Krxt")
        Embed_help.add_field(name="ที่มา", value="แสดงจุดประสงค์ของการสร้างบอทตัวนี้ขึ้นมา", inline=False)
        Embed_help.add_field(name="กิต", value="แสดงผลตอบกลับมาในช่องแชทว่า 'เรื้อน'", inline=False)
        Embed_help.add_field(name="สัญญาณ", value="แสดงผลตอบกลับมาเป็นค่าความคลาดเคลื่อนหรือดีเลย์", inline=False)
        Embed_help.add_field(name="ข้าว", value="สุ่มคำตอบว่าข้าวเที่ยงอยากกินอะไร", inline=False)
        Embed_help.add_field(name="ผู้ใช้", value="แสดงข้อมูลของโปร์ไฟล์ผู้ใช้", inline=False)
        Embed_help.add_field(name="หา", value="หาข้อมูลต่างๆจากวิกิพีเดียโดยใช้ keyword", inline=False)
        Embed_help.add_field(name="ลิงก์", value="แสดงลิงก์ของเวปไซต์ที่ต้องการหาแล้วลิสต์เรียงลงมา(demo)", inline=False)
        Embed_help.set_footer(text="จัดทำโดย นายณฐภัทร กิตติสุทธิ์,นายธนวัฒน์ มีชำนาญ,นายชิษณุพงศ์ รุ่งเรือง")
        await interaction.response.send_message(embed=Embed_help)
        
async def setup(client):
    await client.add_cog(Embed(client))

import discord
from discord.ext import commands 

class Moderation(commands.Cog):
    def __init__(self, client):
      self.client = client
      
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ล้าง(self, ctx, count: int):
      await ctx.channel.purge(limit=count) 
      
      conf_embed = discord.Embed(title="Success", color=discord.Color.orange())
      conf_embed = discord.Embed(title="Success", color=discord.Color.orange())
      conf_embed.add_field(name="System:", value="Message(s) has been delete ", inline=False)
      
      await ctx.send(embed=conf_embed)
                           
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def เตะ(self, ctx, member: discord.Member, *, modreason):
      await ctx.guild.kick(member)
      
      conf_embed = discord.Embed(title="Success", color=discord.Color.orange())
      conf_embed.add_field(name="kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline=False)
      conf_embed.add_field(name="Reason:", value=modreason, inline=False)
      
      await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def แบน(self, ctx, member: discord.Member, *, modreason):
      await ctx.guild.ban(member)
      
      conf_embed = discord.Embed(title="Success", color=discord.Color.orange())
      conf_embed.add_field(name="Banned:", value=f"{member.mention} has been banned from the server by {ctx.author.mention}.", inline=False)
      conf_embed.add_field(name="Reason:", value=modreason, inline=False)
      
      await ctx.send(embed=conf_embed)
    
    @commands.command(name="ปลด")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ปลด(seld, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title="Success", color=discord.Color.orange())
        conf_embed.add_field(name="Unbanned:", value=f"<@{userId}> Congratulation! You has been unbanned from the server by {ctx.author.mention}.", inline=False)
        
async def setup(client):
    await client.add_cog(Moderation(client))
'''
☠☤
表格
666
☠☤
'''

import discord 
from discord.ext import commands
import requests
import random
import os
import asyncio
import json
import schedule,time
from core.classes import cog_Extension
from bs4 import BeautifulSoup

class Reply(cog_Extension):
    
    @commands.command() 

    async def help(self,ctx,neb='1'): 
            await ctx.message.delete()
            d=os.listdir('cmds\\圖片庫')
            seo=len(d)
            if neb=='1' :
                embed = discord.Embed(title="%s"%self.bot.user, description="指令列表:", color=0x0c23f3) 
                embed.add_field(name="~speak (文字)", value="讓%s人說話"%self.bot.user, inline=False) 
                embed.add_field(name="~invoice (發票號碼)", value="對發票用的(只能對財政部最新公布的最新期發票)", inline=False) 
                embed.add_field(name="~stem", value="隨機傳梗圖", inline=False) 
                embed.add_field(name="~figure", value="隨機傳圖(目前有%s張圖)"%seo, inline=False) 
                embed.add_field(name="~info", value="機器人資訊表", inline=False) 
                embed.add_field(name="~help", value="呼叫指令表", inline=False) 
                embed.set_footer(text='第%s/2'%neb)
                await ctx.send(embed=embed)
            
            
            
            
            elif neb=='2':
                embed = discord.Embed(title="%s"%self.bot.user, description="指令列表:", color=0x0c23f3)
                embed.add_field(name="~wo (傳幾個)", value="武漢肺炎的新聞(預設是五個新聞)", inline=False) 
                embed.add_field(name='~ping',value='機器人延遲' ,inline=False)
                embed.add_field(name='~game (數字)',value='猜數字',inline=False)
                embed.add_field(name='~ai (文字)',value='與機器人對話',inline=False)
                embed.set_footer(text='第%s/2'%neb)
                await ctx.send(embed=embed) 

            elif neb=='3' :
                embed = discord.Embed(title="%s"%self.bot.user, description="指令列表:", color=0x0c23f3)
                embed.add_field(name='~tr (翻譯語言) (要翻譯的文字)',value='可以翻譯60種語言',inline=False)
                await ctx.send(embed=embed)
            elif neb=='tr':
                embed=discord.Embed(title='tr指令',url='https://www.itread01.com/content/1542191223.html',color=0x0c23f3)
                embed.add_field(name='翻譯語言的打法',value='請點上方網址查看')
                embed.add_field(name='翻譯文字',value='隨便一國語言都可以請自行試試看很像有支援60個語言而已')
                await ctx.send(embed=embed)
                
            elif neb=='weather' :
                embed = discord.Embed(title='weather指令', color=0x0c23f3)
                embed.add_field(name="~weather (縣市名稱)", value="基本功能記得縣市名稱要寫對喔外島地區目前不支援", inline=False)
                embed.add_field(name="~waether (縣市名稱) week (天數)", value="傳送幾天的天氣預報\n例如:~weather 台北 week", inline=False)
                await ctx.send(embed=embed)
                
    
    
    
    
    @commands.command() 

    async def info(self,ctx): 
        await ctx.message.delete()
        embed = discord.Embed(title="%s"%self.bot.user, description="非常優質的機器人", color=0xeee657)
        embed.add_field(name="作者", value="xiao xigua#8597")
        embed.add_field(name="服務的伺服器數量", value=f"    {len(self.bot.guilds)}") 
        embed.add_field(name="機器人邀請", value="https://discordapp.com/api/oauth2/authorize?client_id=653217150936416256&permissions=8&scope=bot") 
        embed.add_field(name="群組邀請", value="https://discord.gg/q6jkd6U")
        
        await ctx.send(embed=embed) 
    
    









def setup (bot) :
    bot.add_cog(Reply(bot))
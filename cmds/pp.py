import discord 
from discord.ext import commands
import requests
import subprocess
import random
import os
import opus_api,ffmpeg
import asyncio
import json
import schedule,time
import datetime
from bs4 import BeautifulSoup
from core.classes import cog_Extension


with open('JSON\\pos.json','r',encoding='utf-8')  as JSON:
    JSON2=json.load(JSON)
#網路上抓圖片(主函式)
def uu(nem) :
    global io
    ee=random.randint(1,1000)
    use='https://konachan.com/post?page=%d&tags='%ee
    
    use2=requests.get(use)
    t=BeautifulSoup(use2.text,'html.parser')
    u=t.select('#post-list-posts')
    p=u[0].find_all('a')
    io=[]
    for i in range(0,len(p)) :    
        if i%2!=0 :
            r=p[i]['href']
            io.append(r)
#驗證身分組
def w(ctx):

    dpe=ctx.author.roles
    pty=[]
    author=JSON2['ww']
    for p in range(0,len(dpe)) :
        pty.append((str(dpe[p]).split())[0])
    for ppq in range( 0,len(pty)) :
        if str(pty[ppq]) in author :
            op=True   #op如果是True的話就代表有權限
        op=False#如果是False的話沒權限
    return   op    




class Reply(cog_Extension):
    #讓機器人幫你講話
    @commands.command()
    async def speak(self,ctx,*,x):
        await ctx.message.delete()
        await ctx.send(x)



    #網路上抓圖片
    @commands.command()
    async def image(self,ctx,nem=1) :
        nem2=int(nem)
        uu(nem2)

        ip=random.sample(io,nem)
        
        for wp in range(0,len(ip)):
        
            if wp>20 :
                break 
        embed=discord.Embed(title="圖", url=ip[wp], color=0xef10a2)
        embed.set_image(url=ip[wp])    
        await ctx.send(embed=embed)



    #延遲時間
    @commands.command()
    async def ping(self,ctx):
        
        await ctx.send(F'延遲時間:{self.bot.latency*1000}毫秒')
    #刪除訊息
    @commands.command()
    @commands.is_owner()
    async def clean(self,ctx,neb : int):
        await ctx.channel.purge(limit=neb+1)
        await ctx.send(F'已刪除{neb}則訊息')
    #試驗中
    @commands.command()

    async def pp(self,ctx):

        if not ctx.is_nsfw :
            await ctx.send('87')
        else :
            await ctx.send('很抱歉無法傳送')  
    #與機器人對話        
    @commands.command()

    async def ai(self,ctx,x='p'):
        
        if(x=='現在時間'or x=='時間'or x=='time'):
            await ctx.send( time.strftime('20%y-%m-%d-%H:%M:%S'))
        

        
        else :
            problem2 =JSON2['problem']
            if x in problem2.keys() :
                await ctx.send(problem2[x])
            else :
                pop2=JSON2['pop']
                await ctx.send(random.choice(pop2))


def setup (bot) :
    bot.add_cog(Reply(bot))
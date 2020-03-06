import discord 
from discord.ext import commands
import requests
import random
import os
import asyncio
import json
import schedule,time
import datetime
from bs4 import BeautifulSoup
from core.classes import cog_Extension

with open('JSON\\pos.json','r',encoding='utf-8')  as JSON:
    JSON2=json.load(JSON)

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
    @commands.command()

    async def figures(self,ctx):
        await ctx.message.delete()
        


        if w(ctx)==True:
            xx=os.listdir('cmds\\圖片庫')

            
            for i in range(0,len(xx)) :
                    
                y=str(xx[i])
                my_files = discord.File('cmds\\圖片庫\\%s'%(y)),
                await ctx.send(files=my_files)
        else:
            
            
            await ctx.send('你沒有權限使用此指令')
    
    
    
    
    @commands.command() 
    async def figure(self,ctx):
        await ctx.message.delete()
        xx=os.listdir('cmds\\圖片庫')
        
        y=random.sample(xx,1)
        x=str(y[0])
        my_files = discord.File('cmds\\圖片庫\\%s'%(x)),
        
            

        await ctx.send(files=my_files)


    @commands.command()
    async def stem(self,ctx):
        with open('梗圖\\stem.txt','r') as Stem :
            r=Stem.read()
            
            ss=r.split(',')
        s=random.sample(ss,1)
        p=str(s[0])
        await ctx.send(p)
    @commands.command()
    async def image2(self,ctx) :
        ure='https://nekos.life/'
        pt=requests.get(ure)
        pt2=BeautifulSoup(pt.text,'html.parser')
        ttt4=pt2.select('#modal01')
        yyy3=ttt4[0].find_all('img')
        y=yyy3[0]['src']     
        embed=discord.Embed(title='圖',url=y,color=0xef10a2)  
        embed.set_image(url=y) 
        await ctx.send(embed=embed)

    @commands.command()
    async def gif(self,ctx,msg=None):
        if msg==None :
            use='https://tenor.com/'
            use2=requests.get(use)
            t=BeautifulSoup(use2.text, "html.parser")
            yyy=t.select('div[class="Gif"]')
            i=random.randint(0,len(yyy))
            yyy2=yyy[i].find_all('img')
            

            await ctx.send( yyy2[0]['src'])


        else :        
            use='https://tenor.com/search/%s-gifs'%msg
            use2=requests.get(use)
            t=BeautifulSoup(use2.text, "html.parser")
            yyy=t.select('div[class="Gif"]')
            i=random.randint(0,len(yyy))
            yyy2=yyy[i].find_all('img')


            await ctx.send( yyy2[0]['src'])


def setup (bot) :
    bot.add_cog(Reply(bot))
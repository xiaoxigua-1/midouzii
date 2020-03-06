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

from bs4 import BeautifulSoup
from core.classes import cog_Extension
with open('JSON\\pos.json','r',encoding='utf-8') as JSON:
    
    JSON2=json.load(JSON)


class event(cog_Extension):
    
    
    @commands.Cog.listener()
    
    async def on_message(self,msg): 
        JP=JSON2['sp']
        if msg in JP.keys() :
            await msg.channel.send(JSON2[msg])
    
    
    
    @commands.command()
    async def msg(self,ctx,mod= None,*,messages=None) :
        global JSON2
        
        await ctx.message.delete()
        
        if mod==None or messages==None :
            
            await ctx.send('未設定指令參數\n```~msg (指令) (說話)')

            
        else :
            with open('JSON\\pos.json','r') as JJJ:
                JJJ2=json.load(JJJ)
                
                JJJ2['sp'][mod]=messages
            
            JJJ3=json.dumps(JJJ2,indent=2)
            
            
            with open('JSON\\pos.json','w') as pew :
                pew.write(JJJ3)
            
            
            
            with open('JSON\\pos.json','r',encoding='utf-8')  as JSON:
                JSON2=json.load(JSON)
            
            
            await ctx.send(F'已將~{mod}指令新增')

def setup (bot) :
    bot.add_cog(event(bot))
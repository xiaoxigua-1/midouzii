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
class Reply(cog_Extension):
    @commands.command()
    async def tr(self,ctx,Language,msg) :


        subscription_key = "7d26697ce426441c8f0f7533e65b1942"
        trans_base_url = "https://api.cognitive.microsofttranslator.com/"
        trans_url = trans_base_url + 'translate?api-version=3.0'
        headers = {'Ocp-Apim-Subscription-Key':subscription_key}
        params='&to=%s'%Language



        data    = [{'text' : msg}]
        response = requests.post(trans_url, headers=headers,params=params, json=data)
        result = response.json()
        embed=discord.Embed(title='翻譯',color=0x0c23f3)
        embed.add_field(name='輸入語言:',value=result[0]['detectedLanguage']['language'], inline=False)
        embed.add_field(name='翻譯語言',value=result[0]['translations'][0]['to'], inline=False)
        embed.add_field(name='翻譯內容',value=result[0]['translations'][0]['text'], inline=False)




        await ctx.send(embed=embed)






def setup (bot) :
    bot.add_cog(Reply(bot))
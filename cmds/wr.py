'''
我的機器人的prefix是~
目前為支援外島地區跟國外
一般查詢即時天氣資訊指令
~weather (縣市)

EX:~weather 台南
查詢天氣預報
(你的機器人的prefix)weather (縣市) week (天數)
天數預設是3天
最多預報10天
EX:~weather 台北 week
EX:~weather 台北 week 10




'''

import discord 
from discord.ext import commands
import requests
from selenium import webdriver
import random
import os
import asyncio
import json
import schedule,time
from core.classes import cog_Extension
from bs4 import BeautifulSoup


County_table={'桃園':'桃園市','台南':'臺南市','台北':'臺北市','臺北':'臺北市','臺南':'臺南市','台中':'臺中市','高雄':'高雄市','新北':'新北市','基隆':'基隆市','苗栗':'苗栗市','彰化':'彰化市','南投':'南投市','雲林':'雲林市','屏東':'屏東市','宜蘭':'宜蘭市','花蓮':'花蓮市','台東':'台東市'}
class event(cog_Extension):
  @commands.command()
  async def weather(self,ctx,County=None,place=None,Days=3):
      if County=='map' :
        await ctx.send('```下載資料中請稍後....```',delete_after=1)
        d=webdriver.Chrome('./chromedriver') 
        d.implicitly_wait(10)
        d.get('https://www.cwb.gov.tw/V8/C/W/analysis.html')
        d2=BeautifulSoup( d.page_source,'lxml' )
        d3=d2.select('#im')
        d4=d2.select('.slider-btn+ .img-responsive')
        mms1='https://www.cwb.gov.tw/'+d3[0]['src']
        mms='https://www.cwb.gov.tw/'+d4[0]['src']
        d.quit()  
        embed=discord.Embed(title='最新天氣圖',color=0x0c23f3)
        embed.set_image(url=mms)
        embed2=discord.Embed(title='地面天氣圖',color=0x0c23f3)
        embed2.set_image(url=mms1)
        await ctx.send (embed=embed)  
        await ctx.send(embed=embed2)    
      
      
      
      
      
      
      elif place==None :

        
        try :  
            await ctx.send('```下載資料中請稍後....```',delete_after=1)
            url='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8D%97%E5%B8%82/%E8%87%BA%E5%8D%97%E5%B8%82-2306182'
            url2=requests.get(url)
            url3=BeautifulSoup(url2.text,'lxml')
            url4=url3.select('ul[class="My(10px) Tsh($temperature-text-shadow)"]')
            url5=url4[0].find_all('a')
            if County not in County_table.keys() :
              noo=County_table[County]
            elif County in County_table.keys():
              noo=County
            if County=='花蓮' or County=='花蓮縣':
              url6='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%8A%B1%E8%93%AE%E5%B8%82/%E8%8A%B1%E8%93%AE%E5%B8%82-2306187'
            elif County=="雲林" or County=='雲林縣':
              url6='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E9%9B%B2%E6%9E%97/%E9%9B%B2%E6%9E%97-2347346'
              
            
            else :

              for i in range(0,len(url5))  :
                county=str(url5[i]['href']).split('/')
                
                if County_table[County] in county :
                  url6='https://tw.news.yahoo.com'+str(url5[i]['href'])
                  
                  break
                elif County in county :
                  url6='https://tw.news.yahoo.com'+str(url5[i]['href'])
                  break
            url7=requests.get(url6)
            url8=BeautifulSoup(url7.text,'lxml')
            C=url8.select('span[class="Va(t)"]')
            C2=url8.select('span[class="Va(m) Px(6px)"]')
            Information=url8.select('span[class="description Va(m) Px(2px) Fz(1.3em)--sm Fz(1.6em)"]')[0].text
            Body_temperature=url8.select('div[class="Fl(end)"]')[0].text
            Figure=url8.select('div[class="My(2px)"]')[0].find_all('img')[0]['src']
            embed=discord.Embed(title="及時天氣", url=url6,color=0x0c23f3)
            embed.add_field(name="資訊", value=Information, inline=True)
            embed.set_author(name=noo)
            embed.set_thumbnail(url=Figure)
            embed.add_field(name='溫度',value=C[0].text,inline=True)
            embed.add_field(name="最高溫度", value=C2[0].text, inline=True)
            embed.add_field(name="最低溫度", value=C2[1].text, inline=True)
            embed.add_field(name='體感溫度',value=Body_temperature,inline=True)
            embed.set_footer(text=ctx.author)
            await ctx.send(embed=embed)
        except :
          await ctx.send('很抱歉出錯了有可能你輸入錯的名稱也有可能我壞掉了')
      elif place=='week' :
        try :
          await ctx.send('```下載資料中請稍後....```',delete_after=1)
          url='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8D%97%E5%B8%82/%E8%87%BA%E5%8D%97%E5%B8%82-2306182'
          url2=requests.get(url)
          url3=BeautifulSoup(url2.text,'lxml')
          url4=url3.select('ul[class="My(10px) Tsh($temperature-text-shadow)"]')
          url5=url4[0].find_all('a')
          if County not in County_table.keys() :
              noo=County_table[County]
          elif County in County_table.keys():
              noo=County
          if County=='花蓮' or County=='花蓮縣':
              url6='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%8A%B1%E8%93%AE%E5%B8%82/%E8%8A%B1%E8%93%AE%E5%B8%82-2306187'
          elif County=="雲林" or County=='雲林縣':
              url6='https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E9%9B%B2%E6%9E%97/%E9%9B%B2%E6%9E%97-2347346'
              
            
          else :

            for i in range(0,len(url5))  :
                county=str(url5[i]['href']).split('/')
                
                if County_table[County] in county :
                  url6='https://tw.news.yahoo.com'+str(url5[i]['href'])
                  
                  break
                elif County in county :
                  url6='https://tw.news.yahoo.com'+str(url5[i]['href'])
                  break







          url7=requests.get(url6)
          url8=BeautifulSoup(url7.text,'lxml') 
          url9=url8.select('div[class="BdB Bds(d) Bdbc(#fff.12) Fz(1.2em) Py(2px) O(0) Pos(r) forecast-item"]')  
          for p in range(0,Days)  : 
            if p>len(url9)-1 :
              break
            dy=url9[p].find_all('span')[0].text
            rainfall=url9[p].find_all('span')[3].text
            chigh=url9[p].find_all('span')[6].text
            clow=url9[p].find_all('span')[7].text
            Information=url9[p].find_all('span')[1].find_all('img')[0]['title']
            Figure=url9[p].find_all('span')[1].find_all('img')[0]['src']
            
            embed=discord.Embed(title="天氣預報", url=url6, description=dy,color=0x0c23f3)
            embed.add_field(name="資訊", value=Information, inline=True)
            embed.set_author(name=noo)
            embed.set_thumbnail(url=Figure)
            embed.add_field(name="降雨機率", value=rainfall, inline=True)
            embed.add_field(name="最高溫度", value=chigh, inline=True)
            embed.add_field(name="最低溫度", value=clow, inline=True)
            embed.set_footer(text=ctx.author)
            
            await ctx.send(embed=embed)
        except :
          await ctx.send('很抱歉出錯')  
      elif County==None :
        await ctx.send('請輸入縣市或是打\n```~help weather```\n查詢用法')

               


def setup (bot) :
    bot.add_cog(event(bot))
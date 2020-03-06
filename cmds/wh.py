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





class wh(cog_Extension):

    #網路上抓武漢肺炎資料
    @commands.command()
    async def ss(self,ctx,msg=None) :    
        await ctx.message.delete()
        if msg==None :
            

            await ctx.send('```下載資料中請稍後....```',delete_after=1)
            x='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
            p='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
            x2='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
            e2='https://zh.wikipedia.org/wiki/2019%EF%BC%8D2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%96%AB%E6%83%85'
            y=requests.get(x)
            s=BeautifulSoup(y.content,'lxml')
            i=json.loads(s.text)
            j=requests.get(p)
            g=BeautifulSoup(j.content,'lxml')
            f=json.loads(g.text)
            y2=requests.get(x2)
            s2=BeautifulSoup(y2.content,'lxml')
            i2=json.loads(s2.text)
            y3=requests.get(e2)
            ye=BeautifulSoup(y3.text,'lxml')

            yes=ye.select('.wikitable')
            fw=yes[0].find_all('tr')
            for pp in range(0,len(fw)) :

                    ddd=fw[pp].find_all(title='臺灣')
        
                    if len(ddd) !=0 :
                            break
        

        
            fw=yes[0].find_all('tr')
            ss=fw[pp].find_all('td')[1].text
    


            h1=f['features'][0]['attributes']['value']
            h2=i['features'][0]['attributes']['value']
            h3=i2['features'][0]['attributes']['value']

                    
            
            embed=discord.Embed(title='武漢肺炎',color=0x0c23f3,url='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E7%96%AB%E6%83%85')
            embed.add_field(name='全球確診人數',value=h1,inline=False)
            embed.add_field(name='全球死亡人數',value=h2,inline=False)
            embed.add_field(name='全球康復人數',value=h3,inline=False)
            embed.add_field(name='台灣確診人數',value=ss,inline=False)
            await ctx.send(embed=embed)
        elif msg!=None :
            if msg=='韓國' :
                msg='韩国'
            if msg=='臺灣' or msg=='台灣' :
                await ctx.send('```下載資料中請稍後....```',delete_after=1)
                e2='https://zh.wikipedia.org/wiki/2019%EF%BC%8D2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%96%AB%E6%83%85'
                y3=requests.get(e2)
                ye=BeautifulSoup(y3.text,'lxml')
                yes=ye.select('.wikitable')
                fw=yes[0].find_all('tr')
                for pp in range(0,len(fw)) :

                        ddd=fw[pp].find_all(title='臺灣')
            
                        if len(ddd) !=0 :
                                break
            

            
                fw=yes[0].find_all('tr')
                ss=fw[pp].find_all('td')[1].text
                ss1=fw[pp].find_all('td')[2].text
                ss2=fw[pp].find_all('td')[3].text
                embed=discord.Embed(title=msg,color=0x0c23f3,url='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E7%96%AB%E6%83%85')
                embed.add_field(name='確診人數',value=ss,inline=False)
                embed.add_field(name='死亡人數',value=ss1,inline=False)
                embed.add_field(name='康復人數',value=ss2,inline=False)
                embed.set_author(name='武漢肺炎')
                await ctx.send(embed=embed)                
                

            elif msg=='中國' or msg=='中國大陸' or msg=='大陸' :
                await ctx.send('```下載資料中請稍後....```',delete_after=1)
                e2='https://zh.wikipedia.org/wiki/2019%EF%BC%8D2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%96%AB%E6%83%85'
                y3=requests.get(e2)
                ye=BeautifulSoup(y3.text,'lxml')
                yee=ye.select('.sortbottom+ tr td:nth-child(2)')[0].text
                pop=ye.select('.sortbottom+ tr td:nth-child(3)')[0].text
                pop2=ye.select('.sortbottom+ tr td:nth-child(4)')[0].text
                embed=discord.Embed(title=msg,color=0x0c23f3,url='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E7%96%AB%E6%83%85')
                embed.add_field(name='確診人數',value=yee,inline=False)
                embed.add_field(name='死亡人數',value=pop,inline=False)
                embed.add_field(name='康復人數',value=pop2,inline=False)
                embed.set_author(name='武漢肺炎')
                await ctx.send(embed=embed)

            else :
                await ctx.send('```下載資料中....```',delete_after=1)
                e2='https://zh.wikipedia.org/wiki/2019%EF%BC%8D2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%96%AB%E6%83%85'
                y3=requests.get(e2)
                ye=BeautifulSoup(y3.text,'lxml')
                yee=ye.select('.wikitable')[0]
                ye2=yee.find_all('tr')
                pe=[]

                for pp in range(1,len(ye2)-2) :
                    yyy=ye2[pp].find_all('a')[0].text
                    pe.append(yyy)
                    if msg==str(yyy) :
                        break
                if msg not in pe :
                    await ctx.send('你所查詢的國家並沒有資料',delete_after=5)
                else :
                    #確診
                    o=ye2[pp].find_all('td')[1].text
                    #死亡
                    l=ye2[pp].find_all('td')[2].text
                    #康復
                    d=ye2[pp].find_all('td')[3].text
                    embed=discord.Embed(title=msg,color=0x0c23f3,url='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E7%96%AB%E6%83%85')
                    embed.add_field(name='確診人數',value=o,inline=False)
                    embed.add_field(name='死亡人數',value=l,inline=False)
                    embed.add_field(name='康復人數',value=d,inline=False)
                    embed.set_author(name='武漢肺炎')
                    await ctx.send(embed=embed)
            

 
        
        
        
        
        




    #網路上抓有關武漢肺炎的新聞
    @commands.command()
    async def wo(self,ctx,reo=1) :
            await ctx.message.delete()
            e2='https://udn.com/search/word/2/%E6%AD%A6%E6%BC%A2%E8%82%BA%E7%82%8E'
            
            y3=requests.get(e2)
            ye=BeautifulSoup(y3.text,'html.parser')
            yee=ye.select('div[class="story-list__text"]')
            for i in range(0,reo ) :
                    ys=yee[i].find_all('a')
                    yp=yee[i].find_all('time')
                    yy=ys[0].text
                    dd=yee[0].find_all('p')
                    yss=ys[0]['href']
                    yp1=yp[0].text
                    dd1=dd[0].text
                    embed= discord.Embed( title="武漢肺炎", description="有關武漢肺炎的新聞", url=yss, color=0xef10a2) 
                    
                    embed.add_field(name="標題" ,value="%s"%yy, inline=False)
                    embed.add_field(name='內容' ,value='%s'%dd1, inline=False)
                    
                    embed.set_footer(text='新聞發布時間%s'%yp1)
                    if reo>20 :
                        break
                    
                    await ctx.send(embed=embed)



    


    
    #不知道有啥用(就單純更新一下json的資料避免說json改了這裡沒改)
    @commands.command()
    async def json(self,ctx) :
        await ctx.message.delete()
        global JSON2
        with open('JSON\\pos.json','r',encoding='utf-8')  as JSON:
            JSON2=json.load(JSON)
        await ctx.send('資料以更新完成完成')
def setup (bot) :
    bot.add_cog(wh(bot))

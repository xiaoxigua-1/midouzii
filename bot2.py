import discord
import requests,time
import schedule
from discord.ext import commands 
import json
from bs4 import BeautifulSoup
import linebot
bot = commands.Bot(command_prefix='~') 
@bot.event 
async def on_ready(): 
        print('登錄為') 
        print(bot.user.name) 
        print(bot.user.id) 
        print('------')
@bot.command()
async def wo(ctx) :
        e2='https://udn.com/search/word/2/%E6%AD%A6%E6%BC%A2%E8%82%BA%E7%82%8E'

        y3=requests.get(e2)
        ye=BeautifulSoup(y3.text,'html.parser')
        yee=ye.select('div[class="story-list__text"]')
        for i in range(0,len(yee))  :
                ys=yee[i].find_all('a')
                yp=yee[i].find_all('time')
                yy=ys[0].text
                dd=yee[0].find_all('p')
                yss=ys[0]['href']
                yp1=yp[0].text
                dd1=dd[0].text
                await ctx.send('%s\n%s\n%s\n%s'%(yss,yy,dd1,yp1))
        

@bot.command()
async def fff(ctx):
    while 1 :    
        
        x='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
        p='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
        x2='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&cacheHint=true'
        e2='https://zh.wikipedia.org/wiki/2019%EF%BC%8D2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%96%AB%E6%83%85'
        y=requests.get(x)
        s=BeautifulSoup(y.content,'html.parser')
        i=json.loads(s.text)
        j=requests.get(p)
        g=BeautifulSoup(j.content,'html.parser')
        f=json.loads(g.text)
        y2=requests.get(x2)
        s2=BeautifulSoup(y2.content,'html.parser')
        i2=json.loads(s2.text)
        y3=requests.get(e2)
        ye=BeautifulSoup(y3.text,'html.parser')

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

    
        
                
        await ctx.send('全球確診病例:%s\n全球死亡病例:%s\n全球痊癒人數:%s\n台灣確診病例:%s\n\n========='%(h1,h2,h3,ss),delete_after=None)
        time.sleep(120)






bot.remove_command('help') 
bot.run('Njc0NjI4NzE2NjU5NDc0NDky.XjrXKA.G7-RQe7kj4ssZYrMhsyvvou2HcY')


'''
此機器人是中文版
如果你需要英文版
的話就等等看杯
說不定哪天我就會翻譯遺下
哈哈~~
要新增其他功能的話
請到cmds資料夾內
創建一個.py檔
寫在裡面
'''


import discord 
from discord.ext import commands
import requests
import random
import os
import asyncio
import json
import schedule,time

from bs4 import BeautifulSoup

#一些很長的東西通通丟到json檔裡
with open('JSON\\token.json','r',encoding='utf-8') as JSON:
    
    JSON2=json.load(JSON)
    

#機器人的prefix
bot = commands.Bot(command_prefix='*') 
#機器人準備好時執行的
@bot.event 
async def on_ready(): 
        global rand
        print('登錄為') 
        print(bot.user.name) 
        print(bot.user.id) 
        print('------') 
        channel=bot.get_channel(644202847197462550)
        await channel.send('%s機器人已準備好'%bot.user)
        
        rand=random.randint(1,100)


#函式定義區(間單來講就是一些太長的程式碼丟這)
def Redeem2() :
    xiao='http://invoice.etax.nat.gov.tw/'
    
    xiao_xiao=requests.get(xiao)

    bs=BeautifulSoup(xiao_xiao.text,'html.parser')
    global ff,fff,fuck

    data=bs.select('#area1')
    link=data[0].find_all('span')
    fuck=[]
    for n in range(0,len(link)) :
        fuck.append(link[n].text)




    fuck3=str(fuck[3])
    fuck4=str(fuck[4])
    fff=fuck3.split('ã\x80\x81')
    ff=fuck4.split('ã\x80\x81')


def Redeem(invoice) :    
        global Output
        size=[]
        
        Invoice_breakdown=list(invoice)
        
        
        if len(Invoice_breakdown)!= 8 :
            Output='輸入錯誤'
            return Output
            
        tt=''
        tt=Invoice_breakdown[6]+Invoice_breakdown[7]
        tt=Invoice_breakdown[5]+tt
        if invoice==fuck[1] :
            Output='恭喜妳中了特別獎(1000萬元)'
            
        elif invoice==fuck[2] :
            Output='恭喜妳中了特獎(200萬元)'
            
        elif invoice in fff:
            Output='恭喜妳中了頭獎(20萬元)'
            
        elif tt in ff :
            Output='恭喜你中了增開六獎(200元)'
            

        else:
            Jackpot1=str(fff[0])
            Jackpot2=str(fff[1])
            Jackpot3=str(fff[2])
            
            def prize(dd) :    
                
                
                
                
                
                a=7
                for n in range(0,7) :
                    g=a-n
                    if Invoice_breakdown[g]!=dd[g] :
                        break
                

                
                size.append(n)
                
                

            
            if Invoice_breakdown[7]==Jackpot1[7] :
                
                prize(Jackpot1)
                

            if Invoice_breakdown[7]==Jackpot2[7] :
                
                prize(Jackpot2)
                

            if Invoice_breakdown[7]==Jackpot3[7] :
                
                prize(Jackpot3)
                
            

            
            xxxx=max(size)
            if  xxxx==0 or xxxx==1 or xxxx==2:
                Output='非常可惜的沒中獎'
                
            elif xxxx==3  :
                Output='恭喜中了六獎(200元)'
                
            elif xxxx==4 :
                Output='恭喜妳中了五獎(1000元)'
                 
            elif xxxx==5 :
                Output='恭喜你種了四獎(4000元)'
                 
            elif xxxx==6 :
                Output='恭喜你中了三獎(1萬元)'
                
            elif xxxx==7 :
                Output='恭喜你中了二獎(4萬元)'

                
def gam(i):
    
        
        
        global mes,rand
        if i>rand :
            mes='在低一點'
        elif i<rand:
            mes='在高一點'

        else:
            rand=random.randint(1,100)
            mes='你猜對了'
        return mes

    
#猜數字
@bot.command()    
async def game(ctx,p:int):    
    await ctx.send(gam(p))


#對發票

@bot.command()
async def invoice(ctx,invoice) :
    await ctx.message.delete()
    Redeem2()
    Redeem(invoice)
    await ctx.send(Output)






#help定義在embed.py檔裡

bot.remove_command('help') 




#檔案

@bot.command()
@commands.is_owner()
async def load(ctx,extensoin):
    bot.load_extension(F'cmds.{extensoin}')
    await ctx.send('以加載%s檔案'%extensoin)

@bot.command()
@commands.is_owner()
async def unload(ctx,extensoin):
    bot.unload_extension(F'cmds.{extensoin}')
    await ctx.send('以卸載%s檔案'%extensoin)

@bot.command()
@commands.is_owner()
async def reload(ctx,extensoin):
    bot.reload_extension(F'cmds.{extensoin}')
    await ctx.send('以重載%s檔案'%extensoin)


for pew in os.listdir('./cmds') :
    if pew.endswith('.py') :
        bot.load_extension(F'cmds.{pew[:-3]}')

#這個你應該知道
if __name__ == "__main__":
    
    bot.run(JSON2['token'])










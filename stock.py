import twstock 
import time 
import requests

counterLine = 0
counterError = 0

print("Start!")
while True:
    realdata = twstock.realtime.get('2884')  #玉山金
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']
        if float(realprice) >= 25:
            print('目前股價:'+ realprice )
            counterLine =counterLine + 1
            url_ifttt = 'https://maker.ifttt.com/trigger/pttpost/with/key/kiNyQd4NtXnnI46ssJVgBXk3FjE6N1_ttR9cdoCJtpY?value1=250'
            res1 = requests.get(url_ifttt)
            print('第'+str(counterLine) + '次發送LINE回傳訊息:' + res1.text )
        
        if counterError>=3 :
            print("program end!")
            break
        for i in range(300):
            time.sleep(300)   #每五分鐘讀一次

    else:
        print('twstock: read Error')
        print('Due to ' + realdata['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:
            print("program ended")
            break
        for i in range(300):
            time.sleep(300)
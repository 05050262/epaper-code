#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd2in7b.EPD()
epd.init()
def start():
        print("clear")
        epd.Clear(0XFF)
        font32 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 32)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawRe = ImageDraw.Draw(reimage)
        drawBl = ImageDraw.Draw(blimage)
        drawRe.text((80,83),'Lucky Wallet',font = font32, fill = 0)
        epd.display(epd.getbuffer(reimage),epd.getbuffer(blimage))
        time.sleep(2)
        epd.sleep()

def desktop():
        epd.init()
        epd.Clear(0XFF)
        print('desktop')
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.text((30,30),'0.setting',font = font18,fill = 0)
        drawBl.text((30,70),'1.account',font = font18,fill = 0)
        drawBl.text((140,30),'2.transfer',font = font18,fill = 0)
        drawBl.text((140,70),'3.shutdown',font = font18,fill = 0)
        epd.display(epd.getbuffer(blimage),epd.getbuffer(reimage))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next:");
                if int(x) == 0:
                setting()
                elif int(x) == 1:
                        account()
                elif int(x) == 2:
                        transfer()
                #elif int(x) == 3:
                #       shutdown()
                else:
                        continue

def setting():
        epd.init()
        epd.Clear(0XFF)
        print("setting")
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill = 0)
        drawBl.text((70,25),'This is fucking setting',font = font18,fill =0)
        drawBl.text((180,110),'1.privacy',font = font18,fill = 0)
        drawBl.text((25,110),'9.back',font = font18,fill = 0)
        setimage = Image.open('setting.bmp')
        reimage.paste(setimage,(5,5))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next:");
                if int(x) == 1:
                        privacy()
                elif int(x) == 9:
                        desktop()

def account():
        epd.init()
        epd.Clear(0XFF)
        print("account")
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        localtime = time.asctime(time.localtime(time.time()))
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Account name',font = font18,fill =0)
        drawBl.text((70,35),localtime,font = font14,fill =0)
        drawBl.text((180,80),'1.money',font = font14,fill = 0)
        drawBl.text((25,80),'9.back',font = font14,fill = 0)
        accimage = Image.open('account.bmp')
        replyimage = Image.open('reply.bmp')
        blimage.paste(replyimage,(5,121))
        reimage.paste(accimage,(5,5))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next:");
                if int(x) == 1:
                        money()
                elif int(x) == 9:
                        desktop()
                else:
                        continue

def privacy():
        epd.init()
        epd.Clear(0XFF)
        print("privacy")
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Privacy Use',font = font18,fill =0)
        drawBl.text((70,35),'Remember your passwd',font = font14,fill =0)
        replyimage = Image.open('reply.bmp')
        priimage = Image.open('privacy.bmp')
        drawBl.text((180,120),'1.passwd',font = font14,fill = 0)
        blimage.paste(replyimage,(5,121))
        reimage.paste(priimage,(5,5))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next:");
                if int(x) == 1:
                        passwd()
                elif int(x) == 9:
                        setting()
                else:
                        continue

def passwd():
        epd.init()
        epd.Clear(0XFF)
        print("passwd")
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Change your password',font = font18,fill =0)
        drawBl.text((70,35),'Number only',font = font14,fill =0)
        keyimage = Image.open('key.bmp')
        okimage = Image.open('ok.bmp')
        resetimage = Image.open('reset.bmp')
        blimage.paste(okimage,(208,121))
        reimage.paste(keyimage,(5,5))
        blimage.paste(resetimage,(5,121))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(1)
        epd.sleep()
        privacy()

def money():
        epd.init()
        epd.Clear(0XFF)
        print("money")
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Different coin',font = font18,fill =0)
        drawBl.text((70,35),'Watch only',font = font14,fill =0)
        drawBl.text((20,80),'0.00000ETH',font = font18,fill = 0)
        drawBl.text((20,110),'0.00000Bit',font = font18,fill = 0)
        drawBl.text((20,180),'9.back',font = font18,fill = 0)
        monimage = Image.open('money.bmp')
        reimage.paste(monimage,(5,5))
        epd.display(epd.getbuffer(blimage),epd.getbuffer(reimage))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next:");
                if int(x) == 9:
                        account()
                else:
                        continue
def transfer():
        epd.init()
        epd.Clear(0XFF)
        print('transfer')
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((20,140),'9.back',font = font18,fill = 0)
        drawRe.text((90,90),'unfinished',font = font18,fill = 0)
        epd.display(epd.getbuffer(blimage),epd.getbuffer(reimage))
        time.sleep(1)
        epd.sleep()
        while(1):
                x = input("next");
                if int(x) == 9:
                        desktop()
                        
if __name__ == '__main__':
        #start()
        desktop()

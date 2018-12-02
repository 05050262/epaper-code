#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


def setinit(epd):
        epd.init()
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 2$
        font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 1$
        font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 1$
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)

def start(epd):
        print("clear")
        epd.Clear(0XFF)
        drawBl.text((100,83),'Lucky Wallet',font = font24, fill = 0)
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()

def setting(epd):
        epd.init()
        epd.Clear(0XFF)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,25),'This is fucking setting',font = font18,fill =0)
        okimage = Image.open('ok.bmp')
        setimage = Image.open('setting.bmp')
        replyimage = Image.open('reply.bmp')
        blimage.paste(replyimage,(5,121))
        blimage.paste(setimage,(5,5))
        blimage.paste(okimage,(208,121))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()

def account(epd):
        epd.Clear(0XFF)
		localtime = time.asctime(time.localtime(time.time()))
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Account name',font = font18,fill =0)
        drawBl.text((70,35),localtime,font = font14,fill =0)
        monimage = Image.open('money.bmp')
        accimage = Image.open('account.bmp')
        priimage = Image.open('privacy.bmp')
        closeimage = Image.open('shutdown.bmp')
        replyimage = Image.open('reply.bmp')
        blimage.paste(replyimage,(5,121))
        blimage.paste(priimage,(153,121))
        blimage.paste(closeimage,(208,121))
        reimage.paste(accimage,(5,5))
        blimage.paste(monimage,(98,121))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()
def privacy(epd):
        epd.Clear(0XFF)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,10),'Privacy Use',font = font18,fill =0)
        drawBl.text((70,35),'Remember your passwd',font = font14,fill =0)
        replyimage = Image.open('reply.bmp')
        priimage = Image.open('privacy.bmp')
        keyimage = Image.open('key.bmp')
        blimage.paste(replyimage,(5,121))
        reimage.paste(priimage,(5,5))
        blimage.paste(keyimage,(208,121))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()


if __name__ == '__main__':
        epd = epd2in7b.EPD()
        start(epd)
        setting(epd)
        account(epd)
        privacy(epd)

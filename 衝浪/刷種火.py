# -*- encoding=utf8 -*-
__author__ = "JackyWu"

from airtest.core.api import *
connect_device("Android:///")

auto_setup(__file__)
#attack
attack=(1420,760)
att1=(170,630)
att2=(500,630)
att3=(800,630)
att4=(1130,630)
att5=(1460,630)
np1=(480,250)
np2=(800,250)
np3=(1120,250)
npGreen=(420,570)
npBlue=(810,570)
npRed=(1200,570)
#技能
sk1_1=(90,720)
sk1_2=(200,720)
sk1_3=(310,720)
sk2_1=(480,720)
sk2_2=(600,720)
sk2_3=(710,720)
sk3_1=(880,720)
sk3_2=(1000,720)
sk3_3=(1100,720)
#選隊友目標
cm1=(400,550)
cm2=(800,550)
cm3=(1200,550)
#確認
confirm=(1060,520)
cancel=(530,520)
#Master技能
ms=(1490,380)
ms1=(1130,380)
ms2=(1240,380)
ms3=(1350,380)
#交換從者
switch1=(170,450)
switch2=(420,450)
switch3=(670,450)
switch4=(930,450)
switch5=(1180,450)
switch6=(1430,450)
switch_confirm=(800,780)

def choose_friend():
    #swipe((880,840),(740,300))
    find_friend = False
    for i in range(4):
        time.sleep(1)
        if exists(Template(r"tpl1679847250709.png", record_pos=(-0.134, 0.115), resolution=(1600, 900))):
            touch(Template(r"tpl1679847250709.png", record_pos=(-0.134, 0.115), resolution=(1600, 900)))
            find_friend = True
        #elif exists(Template(r"tpl1670813966747.png", threshold=0.9, record_pos=(-0.396, -0.076), resolution=(1600, 900))):
        #    touch(Template(r"tpl1670813966747.png", record_pos=(-0.396, -0.076), resolution=(1600, 900)))
        #    find_friend = True
        #elif exists(Template(r"tpl1677491902651.png", threshold=0.9, record_pos=(-0.398, -0.074), resolution=(1600, 900))):
        #    touch(Template(r"tpl1677491902651.png", record_pos=(-0.398, -0.074), resolution=(1600, 900)))
        #    find_friend = True
        #elif exists(Template(r"tpl1679847413719.png", record_pos=(-0.399, 0.076), resolution=(1600, 900))):
        #    touch(Template(r"tpl1679847413719.png", record_pos=(-0.399, 0.076), resolution=(1600, 900)))
        #    find_friend = True        
        elif i < 3 and not find_friend:
            swipe((880,840),(740,300))
        elif i >= 3 and not find_friend:
            touch(Template(r"tpl1670814147598.png", record_pos=(0.167, -0.181), resolution=(1600, 900)))
            time.sleep(1)
            touch(Template(r"tpl1670814178405.png", record_pos=(0.154, 0.158), resolution=(1600, 900)))
            choose_friend()
        if find_friend:
            break
            
def touch_sleep(cor,second,skip=False):
    touch((cor[0],cor[1]))
    if skip:
        touch((840,460))
    time.sleep(second)

while True:
#if exists(Template(r"tpl1677398785398.png", record_pos=(0.212, -0.171), resolution=(1600, 900))):
 #   touch(Template(r"tpl1677398785398.png", record_pos=(0.212, -0.171), resolution=(1600, 900)))
#if exists(Template(r"tpl1670824996123.png", record_pos=(-0.097, -0.051), resolution=(1600, 900))):
#    touch(Template(r"tpl1670824996123.png", record_pos=(-0.097, -0.051), resolution=(1600, 900)))
#    time.sleep(1)
#    touch(Template(r"tpl1670825061804.png", record_pos=(0.155, 0.158), resolution=(1600, 900)))
    if exists(Template(r"tpl1684072466348.png", record_pos=(-0.099, 0.064), resolution=(1600, 900))):
        touch(Template(r"tpl1684072466348.png", record_pos=(-0.099, 0.064), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl1670825061804.png", record_pos=(0.155, 0.158), resolution=(1600, 900)))
    if exists(Template(r"tpl1670813854855.png", record_pos=(0.401, -0.257), resolution=(1600, 900))):
        time.sleep(1)
        touch(Template(r"tpl1670813871463.png", record_pos=(-0.164, -0.182), resolution=(1600, 900)))
        #touch((540,160))
        time.sleep(1)
        choose_friend()
        if exists(Template(r"tpl1670814249298.png", record_pos=(0.41, 0.244), resolution=(1600, 900))):
            time.sleep(1)
            touch(Template(r"tpl1670814249298.png", record_pos=(0.41, 0.244), resolution=(1600, 900)))
        wait(Template(r"tpl1670814662761.png", record_pos=(0.39, 0.188), resolution=(1600, 900)),timeout=40)
    if exists(Template(r"tpl1670814249298.png", record_pos=(0.41, 0.244), resolution=(1600, 900))):
        time.sleep(1)
        touch(Template(r"tpl1670814249298.png", record_pos=(0.41, 0.244), resolution=(1600, 900)))
        wait(Template(r"tpl1670814662761.png", record_pos=(0.39, 0.188), resolution=(1600, 900)),timeout=40)
    if exists(Template(r"tpl1670814662761.png", record_pos=(0.39, 0.188), resolution=(1600, 900))):
        time.sleep(1)
        touch_sleep(sk3_1,3,True)
        touch_sleep(sk1_1,3,True)
        touch_sleep(sk2_1,3,True)
        touch_sleep(sk1_2,1)
        touch_sleep(cm3,3,True)
        touch_sleep(sk1_3,1)
        touch_sleep(cm3,3,True)
        touch_sleep(sk2_2,1)
        touch_sleep(cm3,3,True)
        touch_sleep(sk2_3,1)
        touch_sleep(cm3,3,True)

        touch_sleep(attack,3)
        touch_sleep(np3,1)
        touch_sleep(att1,1)
        touch_sleep(att2,1)

        wait(Template(r"tpl1670814662761.png", record_pos=(0.39, 0.188), resolution=(1600, 900)),timeout=40)
        touch_sleep(sk3_2,1)
        touch_sleep(npBlue,3,True)
        touch_sleep(sk3_3,3,True)

        touch_sleep(ms,1)
        touch_sleep(ms1,1)
        touch_sleep(cm3,3,True)

        touch_sleep(attack,3)
        touch_sleep(np3,1)
        touch_sleep(att1,1)
        touch_sleep(att2,1)
        
        wait(Template(r"tpl1670814662761.png", record_pos=(0.39, 0.188), resolution=(1600, 900)),timeout=40)
        touch_sleep(ms,1)
        touch_sleep(ms2,1)
        touch_sleep(cm3,3,True)

        touch_sleep(attack,3)
        touch_sleep(np3,1)
        touch_sleep(att1,1)
        touch_sleep(att2,1)

        wait(Template(r"tpl1670816825401.png", record_pos=(-0.34, -0.138), resolution=(1600, 900)),timeout=40)
        
    if exists(Template(r"tpl1670816825401.png", record_pos=(-0.34, -0.138), resolution=(1600, 900))):
        while not exists(Template(r"tpl1670816909527.png", record_pos=(0.365, 0.218), resolution=(1600, 900))):
            touch((820,820))
        if exists(Template(r"tpl1670816909527.png", record_pos=(0.365, 0.218), resolution=(1600, 900))):
            time.sleep(1)
            touch(Template(r"tpl1670816909527.png", record_pos=(0.365, 0.218), resolution=(1600, 900)))
        sleep(1)
    if exists(Template(r"tpl1670816909527.png", record_pos=(0.365, 0.218), resolution=(1600, 900))):
        time.sleep(1)
        touch(Template(r"tpl1670816909527.png", record_pos=(0.365, 0.218), resolution=(1600, 900)))
    if exists(Template(r"tpl1670826092002.png", record_pos=(-0.243, 0.199), resolution=(1600, 900))):
        time.sleep(1)
        touch(Template(r"tpl1670826092002.png", record_pos=(-0.243, 0.199), resolution=(1600, 900)))

    if exists(Template(r"tpl1670817086687.png", record_pos=(0.156, 0.159), resolution=(1600, 900))):
        time.sleep(1)
        touch(Template(r"tpl1670817086687.png", record_pos=(0.156, 0.159), resolution=(1600, 900)))
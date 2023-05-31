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
        if exists(Template(r"tpl1685497596717.png", record_pos=(-0.154, -0.051), resolution=(1600, 900))):
            touch(Template(r"tpl1685497596717.png", record_pos=(-0.154, -0.051), resolution=(1600, 900)))
            find_friend = True
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
    if exists(Template(r"tpl1685501648205.png", record_pos=(0.424, -0.251), resolution=(1600, 900))):
        touch(Template(r"tpl1685501648205.png", record_pos=(0.424, -0.251), resolution=(1600, 900)))
        time.sleep(1)
        touch((800,170))
    if exists(Template(r"tpl1685501823369.png", threshold=0.9, record_pos=(0.388, -0.091), resolution=(1600, 900))):
        touch(Template(r"tpl1685501823369.png", record_pos=(0.388, -0.091), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl1685501871075.png", record_pos=(0.154, 0.159), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl1685501944886.png", record_pos=(-0.002, 0.158), resolution=(1600, 900)))
    for i in range(30):
        touch((600,534))
        time.sleep(0.7)




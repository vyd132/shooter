import wrap
import random

mark=0

def spawn(start):
    buffs = []
    for line in range(0,161,32):
        buff=wrap.sprite.add("mario-scenery",start+line,-50,"block")
        buffs.append(buff)
    number_of_buff=random.randint(-20, 20)
    text=wrap.sprite.add_text(str(number_of_buff),start+64,-65,text_color=[255,255,255],bold=True,font_size=50)
    buff_dict={"id":buffs,"text":text,"buff":number_of_buff,'type':'long'}
    return buff_dict

def line_spawn():
    global mark
    buffs=[]
    for line in range(16,625,208):
        buff=spawn(line)
        buff["mark"]=mark
        buffs.append(buff)
    mark+=1
    return buffs
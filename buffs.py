import wrap
import random



def spawn():
    for wall in range(1,4,1):
        buffs = []
        for line in range(0,160,32):
            buff=wrap.sprite.add("mario-scenery",line+10*wall,-50,"ground")
            buffs.append(buff)
    number_of_buff=random.randint(-5, 5)
    text=wrap.sprite.add_text(str(number_of_buff),x+64,-65,text_color=[255,255,255],bold=True,font_size=50)
    buff_dict={"id":buffs,"text":text,"buff":number_of_buff}
    return buff_dict

def move(object):
    for line in object["id"]:
        wrap.sprite.move(line,0,5)
    wrap.sprite.move(object["text"],0,5)

def remove(object):
    for line in object["id"]:
        wrap.sprite.remove(line)
    wrap.sprite.remove(object["text"])

def y_check(for_el):
    if wrap.sprite.get_y(for_el["id"][0])>=650:
        remove(for_el)
        return True


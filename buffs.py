import wrap
import random

mark=0

# def spawn():
#     global buffs,text
#     number_of_buff = random.randint(-5, 5)
#     lastx=10
#     for wall in range(1,4,1):
#         text = wrap.sprite.add_text(str(number_of_buff),wall*64, -65, text_color=[255, 255, 255], bold=True,font_size=50)
#         buffs = []
#         for line in range(0,161,32):
#             buff=wrap.sprite.add("mario-scenery",lastx+line,-50,"ground")
#             buffs.append(buff)
#         lastx+=192
#     buff_dict={"id":buffs,"text":text,"buff":number_of_buff}
#     return buff_dict

def spawn(start):
    buffs = []
    for line in range(0,161,32):
        buff=wrap.sprite.add("mario-scenery",start+line,-50,"ground")
        buffs.append(buff)
    number_of_buff=random.randint(-5, 5)
    text=wrap.sprite.add_text(str(number_of_buff),start+64,-65,text_color=[255,255,255],bold=True,font_size=50)
    buff_dict={"id":buffs,"text":text,"buff":number_of_buff}
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

def col_check(object,second_id):
    for line in object["id"]:
        if wrap.sprite.is_collide_sprite(line,second_id["id"]):
            remove(object)
            return True

def line_remove(object,spicok):
    for elements in spicok:
        if object['mark']==elements["mark"]:
            remove(elements)
            spicok.remove(elements)

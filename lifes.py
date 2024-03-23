import wrap
import random

hp=100

def spawn():
    lifes_dict={"hp":hp}
    text=wrap.sprite.add_text(str(lifes_dict["hp"]),550,650,text_color=[255,255,255])
    wrap.sprite.set_size_percent(text,125,125)
    lifes_dict["id"]=text
    return lifes_dict

def damage(object):
    object["hp"]-=1
    wrap.sprite_text.set_text(object["id"],str(object["hp"]))

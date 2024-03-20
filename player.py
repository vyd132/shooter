import wrap
import bullet as bul_mod
import time

def spawn():
    plat=wrap.sprite.add("mario-items",50,500,"moving_platform2")
    platform={"id":plat,"perezarydka":0.5,"fire_time":time.time()}
    return platform

def move(object,x):
    wrap.sprite.move_to(object["id"],x,500)

def fire(object):
    b=time.time()
    c=b-object["fire_time"]
    if c >= object["perezarydka"]:
        object["fire_time"]=time.time()
        x=wrap.sprite.get_right(object["id"])
        f_bullets=bul_mod.spawn(x,object)
        s_bullets = bul_mod.spawn(x-64, object)
        return [f_bullets,s_bullets]

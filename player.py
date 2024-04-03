import wrap
import bullet as bul_mod
import time

def spawn():
    plat=wrap.sprite.add("mario-items",50,500,"moving_platform2")
    platform={"id":plat,"perezarydka":0.5,"fire_time":time.time(),"bullets_number":1}
    return platform

def move(object,x):
    wrap.sprite.move_to(object["id"],x,500)

def buff(object,second_id):
    object["bullets_number"]+=second_id["buff"]
    if object["bullets_number"] <=0:
        object["bullets_number"]=1


def fire(object):
    b=time.time()
    c=b-object["fire_time"]
    if c >= object["perezarydka"]:
        bullets=[]
        dist=0
        if object["bullets_number"]==1:
            dist = 32
        object["fire_time"]=time.time()
        x=wrap.sprite.get_left(object["id"])
        for col in range(object["bullets_number"]):
            bullet=bul_mod.spawn(x+dist,object)
            bullets.append(bullet)
            if object["bullets_number"]>1:
                dist+=64/(object["bullets_number"]-1)
                continue

        return bullets

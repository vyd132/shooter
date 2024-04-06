import wrap
import bullet as bul_mod
import time

def spawn():
    plat=wrap.sprite.add("mario-items",50,500,"moving_platform2")
    platform={"id":plat,"perezarydka":0.5,"fire_time":time.time(),"bullets_number":1,"size":64}
    return platform

def move(object,x):
    wrap.sprite.move_to(object["id"],x,500)

def buff(object,second_id):
    if second_id["type"]=='bullet':
        object["bullets_number"]+=second_id["buff"]
        if object["bullets_number"] <=0:
            object["bullets_number"]=1
    if second_id["type"]=='long':
        object["size"] += second_id["buff"]
        if object["size"] < 64:
            object["size"] = 64
        wrap.sprite.set_size(object["id"],object["size"],16)


def fire(object):
    b=time.time()
    c=b-object["fire_time"]
    if c >= object["perezarydka"]:
        bullets=[]
        dist=0
        if object["bullets_number"]==1:
            dist = object['size']/2
        object["fire_time"]=time.time()
        x=wrap.sprite.get_left(object["id"])
        for col in range(object["bullets_number"]):
            bullet=bul_mod.spawn(x+dist,object)
            bullets.append(bullet)
            if object["bullets_number"]>1:
                dist+=object['size']/(object["bullets_number"]-1)
                continue

        return bullets

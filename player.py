import wrap
import bullet as bul_mod

def spawn():
    plat=wrap.sprite.add("mario-items",50,500,"moving_platform2")
    platform={"id":plat}
    return platform

def move(object,x):
    wrap.sprite.move_to(object["id"],x,500)

def fire(object):
    x=wrap.sprite.get_right(object["id"])
    bullets=bul_mod.spawn(x)
    bullets=bul_mod.spawn(x-64)
    return bullets

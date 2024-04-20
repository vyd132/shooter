import wrap

def spawn(x,timer):
    f_bullet=wrap.sprite.add("battle_city_items",x,495,"block_snow")
    wrap.sprite.set_size(f_bullet,6,16)
    bullets={"id":f_bullet,"speed":-10}
    return bullets

def move(object):
    wrap.sprite.move(object["id"],0,object["speed"])


def remove(object):
    wrap.sprite.remove(object["id"])
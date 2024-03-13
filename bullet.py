import wrap

def spawn(x):
    bullet=wrap.sprite.add("battle_city_items",x,495,"block_snow")
    wrap.sprite.set_size(bullet,6,16)
    bullets={"id":bullet,"speed":5}
    return bullets


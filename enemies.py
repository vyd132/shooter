import wrap
import random

def spawn():
    enemies=wrap.sprite.add("mario-enemies",random.randint(50,550),-50,random.choice(["crab","cloud","mushroom"]))
    enemie={"id":enemies,"speed":random.randint(10,20)}
    return enemie

def move(object):
    wrap.sprite.move(object["id"],0,object["speed"])

def remove(object):
    wrap.sprite.remove(object["id"])
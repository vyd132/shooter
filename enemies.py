import wrap
import random
import time

a=time.time()

enemies_col=1

def spawn():
    global enemies_col,a
    enemies_list=[]
    b = time.time()
    c = b - a
    if c >= 5:
        enemies_col+=1
        a = time.time()
    for spawn in range(enemies_col):
        enemies=wrap.sprite.add("mario-enemies",random.randint(50,550),-50,random.choice(["crab","cloud","mushroom"]))
        enemie={"id":enemies,"speed":2}
        enemies_list.append(enemie)
    return enemies_list

def move(object):
    random.randint(-2, 2)
    wrap.sprite.move(object["id"],random.randint(-10,10),object["speed"])
    right=wrap.sprite.get_right(object["id"])
    if right>=600:
        wrap.sprite.move_right_to(object["id"],600)
    left = wrap.sprite.get_left(object["id"])
    if left <= 0:
        wrap.sprite.move_left_to(object["id"], 0)


def remove(object):
    wrap.sprite.remove(object["id"])


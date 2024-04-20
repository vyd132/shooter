import random

import wrap
import player as p_mod, bullet as b_mod,enemies as en_mod,lifes as life_mod, buffs as buff_mod, long_buff as long_mod


width=600
heith=700
wrap.world.create_world(width,heith)

bullets=[]
enemies=[]
buffs=[]

platform=p_mod.spawn()
lifes=life_mod.spawn()



def y_check(spicok,for_el,comand,cord):
    y = wrap.sprite.get_y(for_el["id"])
    if (cord<0 and y <= cord)or(cord >= heith and y >= cord):
        spicok.remove(for_el)
        comand.remove(for_el)
        return True

@wrap.always(5000)
def buff_spwan():
    buff=buff_mod.line_spawn(random.choice(['bullet','long']),True)
    for lists in buff:
        buffs.append(lists)


@wrap.always(500)
def en_spawn():
    enem=en_mod.spawn()
    enemies.extend(enem)

@wrap.on_mouse_move()
def p_move(pos_x):
    p_mod.move(platform,pos_x)

@wrap.on_mouse_down(wrap.BUTTON_LEFT,wrap.BUTTON_RIGHT)
def fire():
    bullet=p_mod.fire(platform)
    if bullet==None:
        return
    bullets.extend(bullet)


@wrap.always()
def b_move():
    for bul in bullets:
        b_mod.move(bul)
        y_check(bullets,bul,b_mod,-50)

@wrap.always()
def buff_move():
    global res
    for buff in buffs.copy():
        buff_mod.move(buff)
        if buff_mod.y_check(buff):
            buffs.remove(buff)
            continue
    for buff in buffs.copy():
        for bul in bullets.copy():
            if buff_mod.armor_check(buff,bul):
                b_mod.remove(bul)
                bullets.remove(bul)
        if buff_mod.col_check(buff,platform):
            if buff_mod.armor_hp_check(buff):
                life_mod.damage(lifes,10)
            else:
                p_mod.buff(platform, buff)
            buff_mod.line_remove(buff, buffs)
            break





@wrap.always()
def en_move():
    for enemie in enemies.copy():
        en_mod.move(enemie)
        if  y_check(enemies, enemie, en_mod, 750):
            life_mod.damage(lifes,1)
            continue
        for bul in bullets.copy():
            res=wrap.sprite.is_collide_sprite(enemie["id"],bul["id"])
            if res:
                b_mod.remove(bul)
                bullets.remove(bul)
                en_mod.remove(enemie)
                enemies.remove(enemie)
                break


import wrap_py
wrap_py.app.start()


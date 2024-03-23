import wrap
import player as p_mod, bullet as b_mod,enemies as en_mod,lifes as life_mod, buffs as buff_mod


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
    buff=buff_mod.spawn()
    buffs.append(buff)

@wrap.always(100)
def en_spawn():
    enem=en_mod.spawn()
    enemies.append(enem)


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
    for buff in buffs.copy():
        buff_mod.move(buff)
        if buff_mod.y_check(buff, buff_mod):
            buffs.remove(buff)
            continue
        # for bul in bullets.copy():
        #     res = wrap.sprite.is_collide_sprite(buff["id"], bul["id"])
        #     if res:
        #         b_mod.remove(bul)
        #         bullets.remove(bul)
        #         bul["bullets_number"]=buff["buff"]
        #         buff_mod.remove(buff)
        #         buffs.remove(buff)
        #         break



@wrap.always()
def en_move():
    for enemie in enemies.copy():
        en_mod.move(enemie)
        if  y_check(enemies, enemie, en_mod, 750):
            life_mod.damage(lifes)
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


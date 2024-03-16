import wrap
import player as p_mod, bullet as b_mod,enemies as en_mod

width=600
heith=700
wrap.world.create_world(width,heith)

bullets=[]
enemies=[]

platform=p_mod.spawn()

@wrap.always(3000)
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



@wrap.always()
def en_move():
    for enemie in enemies.copy():
        en_mod.move(enemie)
        for bul in bullets.copy():
            res=wrap.sprite.is_collide_sprite(enemie["id"],bul["id"])
            if res:
                b_mod.remove(bul)
                bullets.remove(bul)
                en_mod.remove(enemie)
                enemies.remove(enemie)


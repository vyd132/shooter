import wrap
import player as p_mod

width=600
heith=700
wrap.world.create_world(width,heith)

bullets=[]

platform=p_mod.spawn()

@wrap.on_mouse_move()
def p_move(pos_x):
    p_mod.move(platform,pos_x)

@wrap.on_mouse_down(wrap.BUTTON_LEFT,wrap.BUTTON_RIGHT)
def fire():
    bullet=p_mod.fire(platform)
    bullets.append(bullet)


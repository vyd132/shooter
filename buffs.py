import time
import wrap
import random
import bullet as bul_mod

size=16
mark=0

# def spawn():
#     global buffs,text
#     number_of_buff = random.randint(-5, 5)
#     lastx=10
#     for wall in range(1,4,1):
#         text = wrap.sprite.add_text(str(number_of_buff),wall*64, -65, text_color=[255, 255, 255], bold=True,font_size=50)
#         buffs = []
#         for line in range(0,161,32):
#             buff=wrap.sprite.add("mario-scenery",lastx+line,-50,"ground")
#             buffs.append(buff)
#         lastx+=192
#     buff_dict={"id":buffs,"text":text,"buff":number_of_buff}
#     return buff_dict

def spawn(start,number_of_buff,type,armor_ask):
    buffs = []
    buff_dict ={"buff": number_of_buff, 'type': type,'mark':None}
    costume='ground' if type=='bullet' else 'block'
    for line in range(0, 161, 32):
        buff = wrap.sprite.add("mario-scenery", start + line, -50, costume)
        buffs.append(buff)
    if armor_ask:
        armor_spawn(start,buff_dict)
    buff_dict['id']=buffs
    text = wrap.sprite.add_text(str(number_of_buff), start + 64, -65, text_color=[255, 255, 255], bold=True,font_size=50)
    buff_dict["text"]=text
    return buff_dict



def armor_spawn(start,buff):
    armor=wrap.sprite.add('battle_city_items',start+80,-45,"base_defend_steel")
    buff["armor_size"] = 5
    wrap.sprite.set_size(armor,160,size)
    buff["armor"]=armor
    buff['size']=16


def line_spawn(type,ask):
    global mark
    buffs=[]
    for line in range(16,625,208):
        buff=spawn(line,random.randint(-7,5),type,ask)
        buff["mark"]=mark
        buffs.append(buff)
    mark+=1
    return buffs
def move(object):
    for line in object["id"]:
        wrap.sprite.move(line,0,5)
    wrap.sprite.move(object["text"], 0, 5)
    if 'armor' in object:
        wrap.sprite.move(object["armor"], 0, 5)




def remove(object):
    for line in object["id"]:
        wrap.sprite.remove(line)
    wrap.sprite.remove(object["text"])
    if 'armor' in object:
        wrap.sprite.remove(object["armor"])

def y_check(for_el):
    if wrap.sprite.get_y(for_el["id"][0])>=650:
        remove(for_el)
        return True

def col_check(object,second_id):
    '''
    Проверка столкнулась ли платформа со спрайтом и возвращение результата
    :return:
    '''
    for line in object["id"]:
        if wrap.sprite.is_collide_sprite(line,second_id["id"]):
            return True

def armor_check(object,second_id):
    global size
    '''


    :return:
    '''
    if 'armor' in object:
        print("work")
        if wrap.sprite.is_collide_sprite(object['armor'], second_id['id']):
            print("work1")
            object["armor_size"] -= 1
            object['size']=object['size']-16/5
            wrap.sprite.set_size(object["armor"], 160,object["size"])
            return True

'''
После того как все платформы сдвинулись
    если платформа коснулась с пулей И есть броня
        уменьшаем размер брони
        удаляем пулю
    если платформа коснулась с игроком
        удаляем линию
        если есть броня И больше 0 жизней
            наносим урон игроку
        иначе 
            начисляем бонус
                
'''

def line_remove(object,spicok):
    for elements in spicok.copy():
        if object['mark']==elements["mark"]:
            remove(elements)
            spicok.remove(elements)

def armor_hp_check(object):
    if 'armor' in object and object["armor_size"] > 0:
        return True
    return False
import time
import auto_player as player
from settings import *

def get_pictures(id, bbox):
    return player.save_shot_box(id, bbox)

def houyuan_zhiding():
    for id in ids:
        print(id)
        player.find_touch('baifang')
        player.find_touch('input')
        player.find_touch('kuang')
        player.type(id)
        player.find_touch('finish')
        player.find_touch('query')
        player.find_touch('visit')
        time.sleep(2)
        player.find_touch('mache')
        time.sleep(1)
        get_pictures(id, (0, 80, 450, 800))
        player.find_touch_any(['close', 'close1'])
        player.find_touch('home')
        time.sleep(2)

if __name__ == '__main__':
    houyuan_zhiding()

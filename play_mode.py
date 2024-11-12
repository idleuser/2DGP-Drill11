import random

from pico2d import *
import game_framework

import game_world
import title_mode
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global zombies

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    balls = [Ball(random.randint(100,1500),60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    # 충돌 정보를 등록
    game_world.add_collision_pair('boy-ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy-ball', None, ball)
    # 좀비 - 소년
    game_world.add_collision_pair('boy-zombie',boy,None)
    for zombie in zombies:
        game_world.add_collision_pair('boy-zombie', None, zombie)
        game_world.add_collision_pair('fireball-zombie', None, zombie)




def finish():
    game_world.clear()
    pass


def update():
    game_world.update() # 소년과 볼 위치가 다 업데이트 완료
    game_world.handle_collisions()

    # 아마추어
    # for ball in balls.copy():
    #     if game_world.collide(boy, ball):
    #         print('boy:ball COLLIDE')
    #         # 소년 볼 증가
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass


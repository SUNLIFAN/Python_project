from settings import Settings

from ship import Ship

import game_functions as gf

import pygame

from pygame.sprite import Group

from Alien import Alien
def run_game():
	#初始化游戏、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船
	ship = Ship(screen,ai_settings)
	#创建用于存储子弹的编组
	bullets  = Group()
	#创建aliens编组
	aliens = Group()
	#创建Ailens群
	gf.create_fleet(ai_settings,screen,aliens,ship)
	#开始游戏的主循环
	while True:

		#监听键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_aliens(aliens,ai_settings)
		#更新屏幕
		gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()
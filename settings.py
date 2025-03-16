import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
coins_count = 0
is_key = False



window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Platformer Dino")
pygame.display.set_icon(pygame.image.load("assets/images/player/stand_1.png"))

clock = pygame.time.Clock()
"""ГРУПИ СПРАЙТІВ"""
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
"""КАРТИНКИ СПРАЙТІВ"""
bg = pygame.transform.scale(pygame.image.load("assets/backgrounds/bg1.jpg"), (W, H))

platform_image = pygame.image.load("assets/backgrounds/platform.png")
player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]

coin_image = pygame.image.load('assets/images/coins/coin.png')
key_image = pygame.image.load("assets/images/key/key.png")
chest_image = pygame.image.load("assets/images/chest/chest.png")
portal_image = pygame.image.load("assets/images/portal/portal.png")
"""ШРИФТИ"""
pygame.font.init()
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 80)

"""ТЕКСТИ"""
find_key_txt = font2.render("Знайди ключ", True,(255,255,255))
open_chest_txt =  font2.render(" Натисни є щоб відкрити", True,(255,255,255))
get_key_txt = font2.render("Натисни е щоб відкрити", True,(255,255,255))
from objects import *
from levels import *

pygame.init()

level1_objects, key, chest = draw_level(level1)
player = Player(50, H - 90, 40, 50, 10, player_images)
portal = MapObject(1000, 500, 50, 50, portal_image)  

level1_objects.add(portal)
level1_objects.add(player)


game = True
while game:
    key_pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.blit(bg, (0, 0))
    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)

    player.update(platforms)
    
    if pygame.sprite.spritecollide(player, coins, True):
        coins_count += 1
        
    window.blit(pygame.transform.scale(coin_image, (40, 40)), (10,10))
    coins_txt = font1.render(f":{coins_count}", True, (255, 255, 255))
    window.blit(coins_txt, (55, 12))
    
    if pygame.sprite.collide_rect(player, key):
        window.blit(get_key_txt,( W // 2 -300, 50))
        if key_pressed[pygame.K_e]:
            is_key = True
            key.rect.x = -200
    
    if pygame.sprite.collide_rect(player, chest) and is_key:
        window.blit(open_chest_txt,( W // 2 -300, 50))
        if key_pressed[pygame.K_e]:
            coins_count += 20
            chest.rect.x = -300
            
    if pygame.sprite.collide_rect(player, chest) and not is_key:
        window.blit(find_key_txt, ( W // 2 -300, 50))
    


    pygame.display.update()
    clock.tick(FPS)
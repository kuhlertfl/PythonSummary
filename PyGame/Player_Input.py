#2 Different ways for a player to input something 
#1. Event loop (in the for loop)
import pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #event will trigger if mouse is moved
        if event.type == pygame.MOUSEMOTION: #.MOUSEBUTTONDOWN: .MOUSEBUTTONUP:
            if player_rect.collidepoint(event.pos):
                print("player")
            pass
        #Keyboard input in the event loop --> check if any button was pressed --> work with a specific key 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")
        if event.type == pygame.KEYUP:
            print("key up")

#2. KeyBoard input 
#====================================================
#KEYBOARD INPUT (in the while loop)
#====================================================
# keys = pygame.key.get_pressed()
# if keys[pygame.K_SPACE]:
#     print("jump")
#====================================================
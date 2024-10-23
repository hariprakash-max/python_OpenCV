import pygame

pygame.init()
display_surface = pygame.display.set_mode((800,500))
done = False

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
              pygame.quit()
              quit()
    pygame.draw.rect(display_surface,(255,0,0),
    pygame.Rect(40,30,100,100))

    pygame.display.flip()
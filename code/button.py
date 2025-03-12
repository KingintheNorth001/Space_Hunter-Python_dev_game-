
import pygame
#button class
class Button:
    def __init__(self , screen , x, y, image,  img_wid, img_height):
        width = img_wid
        height = img_height
        self.screen = screen
        self.image = pygame.transform.scale(image , (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked  = False

    def draw(self):
        #get mouse positon
        action = False
        pos = pygame.mouse.get_pos()
        #check mouse over buttons
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


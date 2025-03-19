#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png") # Loading the menu background image
        self.rect = self.surf.get_rect(left=0, top=0) # Defining a transparent rectangle to position the menu image



    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)# "blit" will draw the image (Ensuring it appears within the rectangle)

        pygame.display.flip() # Atualizar


        pass

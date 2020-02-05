from tkinter import *
import pygame
import random
import os

root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0, column=0)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
pygame.display.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.flip()
button = Button(root, text='ok')
button.grid(row=1, column=0)
while True:
    # your code here
    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.display.flip()
    root.update()

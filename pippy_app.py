#!/usr/bin/python
# -*- coding: utf-8 -*-
# bounce: move some text around the screen

import pippy, pygame, sys
from pygame.locals import *
from random import *

# always need to init first thing
pygame.init()

# turn off cursor
pygame.mouse.set_visible(False)

# XO screen is 1200x900
size = width, height = 1200, 900

# we'll use 36 pixel high text
fsize = 36

# vector for motion, will control speed and angle
mvect = [3,2]

# create the window and keep track of the surface
# for drawing into
screen = pygame.display.set_mode(size)

msg = "I am your screensaver!!!"

# create a Font object from a file, or use the default
# font if the file name is None. size param is height
# in pixels

# usage: pygame.font.Font(filename|object, size)
font = pygame.font.Font(None, fsize)

# Font.render draws text onto a new surface.
#
# usage: Font.render(text, antialias, color, bg=None)
text = font.render(msg, True, (10,10,10))

# the Rect object is used for positioning
textRect = text.get_rect()

# start at the top left
textRect.left = 0;
textRect.top = 0;

while pippy.pygame.next_frame():

  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()

    elif event.type == KEYDOWN:
      sys.exit()

  screen.fill((250,250,250))
  
  # draw the text
  screen.blit(text, textRect)

  # update the display
  pygame.display.flip()

  # move the text
  #
  # Rect.move returns a new Rect while
  # Rect.move_ip moves in place, so we'll use
  # the latter
  textRect.move_ip(mvect)

  # bounce off edges
  if textRect.left < 0 :
    textRect.left = 0
    mvect[0] = -1 * mvect[0]
  elif textRect.right >= size[0] :
    textRect.right = size[0] - 1
    mvect[0] = -1 * mvect[0]

  if textRect.top < 0 :
    textRect.top = 0
    mvect[1] = -1 * mvect[1]
  elif textRect.bottom >= size[1] :
    textRect.bottom = size[1] - 1
    mvect[1] = -1 * mvect[1]

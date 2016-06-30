#!/usr/bin/env python

# This prints instructions to screen
print("""
This example turns your Explorer HAT into a drum kit!

Hit any touch pad to hear a drum sound.

Press CTRL+C to exit.
""")

# The next three statements imports python libraries for our code to use
import signal
import pygame
import explorerhat

# The next block of code creates an array of sopund files to use
samples = [
    'sounds/hit.wav',
    'sounds/thud.wav',
    'sounds/crash.wav',
    'sounds/smash.wav',
]


# This is initialising pygame to play the sound files
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

sounds = []
for x in range(4):
    sounds.append(pygame.mixer.Sound(samples[x]))
    
def handle(ch, evt):
    if evt == 'press':
        sounds[ch - 5].play(loops=0)
        #name = samples[ch - 5].replace('sounds/','').replace('.wav','')
        #print("{}!".format(name.capitalize()))

explorerhat.touch.pressed(handle)
explorerhat.touch.released(handle)

signal.pause()


    

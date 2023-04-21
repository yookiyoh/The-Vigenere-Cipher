# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming - Assignment 2 - Problem 3

import pygame
import random

# Define the font for Pygame
pygame.font.init()
font = pygame.font.SysFont("monospace", 48)

# Define the character substitute dictionary
sub_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
            'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Get the plaintext and keyword from user input
plaintext = input("Enter a message (all uppercase, no spaces): ")
keyword = input("Enter a keyword (all uppercase): ")

# Encrypt the plaintext using the Vigenere cipher
ciphertext = ""
keyword_index = 0
for char in plaintext:
    if char not in sub_dict:
        # Ignore non-letter characters
        ciphertext += char
        continue
    # Convert the letter to its corresponding number value
    plaintext_num = sub_dict[char]
    keyword_num = sub_dict[keyword[keyword_index]]
    # Calculate the ciphertext number value
    ciphertext_num = (plaintext_num + keyword_num) % 26
    # Convert the ciphertext number value back to its corresponding letter
    ciphertext += list(sub_dict.keys())[list(sub_dict.values()).index(ciphertext_num)]
    # Update the keyword index to wrap around to the beginning of the keyword if necessary
    keyword_index = (keyword_index + 1) % len(keyword)

# Create the Pygame window and display the ciphertext
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Vigenere Cipher")

# Create a white star background
stars = []
for i in range(100):
    x = random.randint(0, size[0] - 1)
    y = random.randint(0, size[1] - 1)
    stars.append((x, y))
for star in stars:
    pygame.draw.polygon(screen, (255, 255, 255), [(star[0], star[1] - 3), (star[0] + 3, star[1]), (star[0], star[1] + 3), (star[0] - 3, star[1])])

# Create the ciphertext surface 
ciphertext_surface = font.render(ciphertext, True, (255, 255, 255))

# Center the ciphertext on the screen
ciphertext_x = (size[0] - ciphertext_surface.get_width()) / 2
ciphertext_y = (size[1] - ciphertext_surface.get_height()) / 2

# Blit the ciphertext onto the screen
screen.blit(ciphertext_surface, (ciphertext_x, ciphertext_y))

pygame.display.flip()
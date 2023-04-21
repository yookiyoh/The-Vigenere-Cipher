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
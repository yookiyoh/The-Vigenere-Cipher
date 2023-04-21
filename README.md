# The-Vigenere-Cipher
OOP CMPE 103 Lab Exercise 1

# Problem 3: The Vigenère Cipher

The Vigenère Cipher works as follows:

Your key is a keyword, which you then translate into corresponding letter values 0 – 25. Then, to encrypt, write your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result mod 26. These resultant numbers are the ciphertext.

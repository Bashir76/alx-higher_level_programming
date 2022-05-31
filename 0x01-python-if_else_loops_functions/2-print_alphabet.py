#!/usr/bin/python
"""Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line."""
for latter in range(97, 123):
   print("{}".format(chr(latter)), end="")

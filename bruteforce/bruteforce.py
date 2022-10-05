import requests

with open("passwords.txt") as f:
  guesses = f.readlines()

for password in guesses:
  
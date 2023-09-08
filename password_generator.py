#hello there today we are going to build a password generator
import random #this library will help us build the project

def gen(p_length):
	chars = "azertyuiopqsdfghjklmwxcvbn1234567890@/.;:§!?_-|{}&[]()=''``+*µ¤$£²"
	list_chars = list(chars) #list() will put each char in the chars variable inside an array

	password_chars = []
	password = ""

	for i in range(p_length):
		random_char = random.choice(list_chars)
		password_chars.append(random_char)
	for char in password_chars:
		password += char
	return password
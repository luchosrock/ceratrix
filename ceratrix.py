#!/bin/python

import random

with open("letras.md") as f:
	content = f.readlines()

for i in range(1,10):
	print(random.choice(content)),
	if(i%4==0):
		print("")
print("...")

# -*- coding: utf-8 -*-
__author__ = 'Xiaoming'

import random,string

def get_charint(width = 4, num = 200):
	charint = string.digits + string.letters
	for i in range(num):
		verify = [random.choice(charint) for j in range(width)]
		verify = ''.join(verify) + '\n'
		# verify =random.choice(charint)
		# for i in range(width):
		# 	verify = verify + random.choice(charint)
		print verify
	return verify

if __name__ == "__main__":
	get_charint()
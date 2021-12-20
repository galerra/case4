# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
	A = [int(a) for a in input().split()]
	s = 1
	if len(A) < 10:
		print('Введен массив, который меньше 10 элементов')
	else:
		for i in A:
			if i > 0:
				s *= i
		print(s)
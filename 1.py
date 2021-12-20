# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
	A = [int(a) for a in input().split()]
	if len(A) < 10:
		print('Введен массив, который меньше 10 элементов')
	else:
		m = max(A)
		i_m = A.index(m)
		A[0], A[i_m] = A[i_m], A[0]
		print(A)

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
	import math
	A = [float(a) for a in input().split()]
	a = round(sum(A[0::2]),2)
	sp = []
	s = 0
	for i in A:
		if i < 0:
			sp.append(i)
			break
	A.reverse()
	for j in A:
		if j < 0:
			sp.append(j)
			break
	if len(sp) > 1:
		print(sp)
		A.reverse()
		i_1 = A.index(sp[0])
		i_2 = A.index(sp[1])
		s = round(sum(A[(i_1+1):i_2:1]),2)
		print(A[(i_1+1):i_2:1])
	print('Сумма элементов с нечетным индексом:',a)
	print('Сумма чисел между первым и последним отрицательным:',s)
	N = []
	for k in A:
		if math.sqrt(k * k) < 1:
			N.append(k)
	for m in N:
		A.remove(m)
	for i in range(len(N)):
		A.append(0)
	print('Сжатый список:',A)
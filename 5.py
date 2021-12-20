
# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = float(input())
    b = float(input())
    sp = list(map(float, input().split()))
    print(max(sp))
    num = list()
    for i in sp:
        if i > 0:
            num.append(i)
    last = sp.index(num[-1])
    s = sum(sp[:last])
    print(s)
    for i in range(len(sp)):
        if a <= abs(sp[i]) <= b:
            sp[i] = 0
    print(sp)
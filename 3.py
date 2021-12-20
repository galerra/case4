# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = list()
    for i in range(10):
        a.append(int(input()))
    sm = a.index(min(a))
    a[-1], a[sm] = a[sm], a[-1]

    print(a)
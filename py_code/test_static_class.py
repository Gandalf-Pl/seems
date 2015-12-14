# -*- coding: utf-8 -*-

class A(object):
    NUM = 1

if __name__ == "__main__":
    a1 = A()
    a2 = A()

    print a1.NUM  # 1
    print a2.NUM  # 1

    A.NUM = 3

    print a1.NUM # 3
    print a2.NUM # 3

    a1.NUM = 10
    print a1.NUM # 10
    print a2.NUM # 3

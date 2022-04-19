# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:56:59 2022

@author: USER
"""

""" Python 練習
題目：將一個正整數分解質因數。例如：輸入90,打印出90=2*3*3*5。
程式分析：對n進行分解質因數，應先找到一個最小的質數k，然後按下述步驟完成：
(1)如果這個質數恰等於n，則說明分解質因數的過程已經結束，打印出即可。
(2)如果n<>k，但n能被k整除，則應打印出k的值，並用n除以k的商,作為新的正整數你n,重複執行第一步。
(3)如果n不能被k整除，則用k+1作為k的值,重複執行第一步。
"""

def reduceNum(n):
    print ('{} = '.format(n), end=" ")
    if not isinstance(n, int) or n <= 0 :
        print ('請輸入一個正確的數字 !')
        exit(0)
    elif n in [1] :
        print ('{}'.format(n))
    while n not in [1] : # 迴圈保證遞迴
        for index in range(2, n + 1) :
            if n % index == 0:
                n //= index # n 等於 n//index
                if n == 1: 
                    print (index )
                else : # index 一定是素數
                    print ('{} *'.format(index), end=" ")
                break
# reduceNum(90)
# reduceNum(100)
reduceNum(720)
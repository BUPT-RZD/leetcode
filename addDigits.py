# -*- coding: utf-8 -*-
#思路：取各位数字相加，直至相加结果为一位数（<9），考虑边界情况
class Solution(object):
    def addDigits(self, num):
        a=[]
        while num>9:
            #考虑边界情况
            while num >0:
                b=num%10
                a.append(b)
                num=(num-b)/10        
                alen = len(a)
            for i in range(0,alen):
                num+=a[i]
            a=[]
        return num
#思路：规律是直接与9的取余            
class Solution(object):
    def addDigits(self, num):
        if num==0:
            num=0
        elif num%9==0:
            num=9
        else:
            num=num%9
        return num

    

# -*- coding: utf-8 -*-
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
            
    

    

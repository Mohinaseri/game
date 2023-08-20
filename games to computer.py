# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:57:21 2023

@author: Mohadese
"""

a=int(input("please enter your once number:"))
b=int(input("please enter your twice number:"))

import random
hads=random.randint(a,b)

javab=int(input("please enter your number:"))

while javab!=hads:
    
 
    if hads<javab :
        a=hads
    elif javab<hads:
        b=hads
    
    hads=random.randint(a,b)
    print(hads)
    
print("woooooowww you can computer:))")


#ما در این برنامه از کامپیوتر میخواهیم یک حدس بینااعداد انتخابی ما بزند و ما به عنوان کاربر بررسی کنیم ایا کامپیوتر عدد مورد نظر ما را درست حدس زده و در این بازی پیروز شده است یا خیر؟ 
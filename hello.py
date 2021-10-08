# import math as m
# import numpy as np
# sin,cos,tan,cot,sec,cosec,log,cosh= lambda angle :print( np.sin(np.radians(angle)).astype(int)),lambda angle :print( np.cos(np.radians(angle)).astype(int)),lambda angle : print(np.tan(np.radians(angle)).astype(int)),lambda angle:print(np.cot(np.radians(angle)).astype(int)),lambda angle:print(np.sec(np.radians(angle)).astype(int)),lambda angle : print(np.cosec(np.radians(angle)).astype(int)),lambda number : print(m.log(number)),lambda number : print(np.cosh(np.radians(number)).astype(int))
# print('hii there stranger')
# lol = input('tell me ur name  : ')
# print(f'okk {lol} , please continue using the calculator, type done after your work is done...')
# print('*'*69)
# while True:
#     try:
#         x = input('here : ')
#         if x != 'done':print(f'{lol}, your answer is = {eval(x)}')
#         else:
#             print(f'try again {lol}')
#             break
#     except: continue
# print(f'thank u for using the calcy {lol}'),print('*'*69)
#  !(T_T)
# from typing import List


from collections import defaultdict
names = ["Adam","Aryan" ,"Bea", "Charlie", "Danielle","Eve", "Frantz", "Gustav", "Helena"]

cad = defaultdict(list)
for i in names : 
    cad[i[0]].append(i)

print(cad)


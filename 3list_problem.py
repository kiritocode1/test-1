
# TODO :  make a namedtuple or a dataframe , easily . 	
from collections import namedtuple
from typing import Any
def answer():
    no_of_students=int(input("here ---> "))
    columns_of_adjectives = input("the columns of data here ---> ").split()
    a = namedtuple("fofo" , columns_of_adjectives)
    list_of_students = []
    for i in range(no_of_students):
        data = input("here----> ").split()
        xyz = a(*data)
        list_of_students.append(xyz)
    return print(list_of_students)
answer()

#! ///////////////////////////////////////////////////////////////////////////////////////////////////////
#  TODO: u have 3 lists find the min index with sum given 
def finalFantasy(x:list, y: list , z: list , a:int)->Any:
    ''' this code is essentially the same as n diff
    i made but hey it's awesome :) 
    
    x --->[1,2,3]
    y --->[4,5,6]
    z --->[7,8,9] 
    this code does take care because iteration will return the minimum
    index. 
    '''
    for i in range(len(x)):
        for j in range(len(x)):
            diff = a-(x[i]+y[j])
            try: return [i , j , z.index(diff)]
            except: continue
    return None







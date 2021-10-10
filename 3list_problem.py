

# TODO :  make a namedtuple or a dataframe , easily . 	
from collections import namedtuple
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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
#  TODO: u have 3 lists find the min index with sum given 
def finalFantasy(x:list, y: list , z: list , a: int):
    for i in range(len(x)):
        for j in range(len(x)):
            diff = a-(x[i]+y[j])
            try: return [i , j , z.index(diff)]
            except: continue







# TODO: to make  some shit

# def foo(n):
#     nice= nt("fofo" ,input("here--->"))
#     list1 = []
#     for i in range(n):

# Python code to demonstrate namedtuple()
	
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

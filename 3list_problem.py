
# TODO: to make  some shit

# def foo(n):
#     nice= nt("fofo" ,input("here--->"))
#     list1 = []
#     for i in range(n):

# Python code to demonstrate namedtuple()
	
from collections import namedtuple
	
# # Declaring namedtuple()
# Student = namedtuple('Student',['name','age','DOB'])
	
# # Adding values
# S = Student('Nandini','19','2541997')
	
# # Access using index
# print ("The Student age using index is : ",end ="")
# print (S[1])
	
# # Access using name
# print ("The Student name using keyname is : ",end ="")
# print (S.name)
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
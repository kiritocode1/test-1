
from typing import Counter, List, OrderedDict
import math as m


class project_euler:
    '''
    INTRODUCTION:
    practicing some of the most hardest coding and mathematical problems.
    copyleft by projecteuler.net 
    please dont sue me , show them some love 🖤🖤🖤
    '''
    def e1() -> int:
        ''' to find the multiples of all nos between 3 and  5 in 1000

        '''
        a = sum(list(filter(lambda x: x % 3 == 0 and x %
                5 == 0, [i for i in range(1000)])))
        return a

    def e2(x=1000) -> list[int]:
        '''
        [0,1,2,3,4,5,6,7,8,9,10]->[0,1,1,3,5,7,9,]
        to run a fibonnaci series  in one minuite , upto x steps  
        '''
        a = 0
        l = []
        for i in range(1, x+1):
            l.append(a)
            a = a+i
        l2 = list(filter(lambda x: x % 2 == 0, l))
        return l2

    def e3():
        '''
        TODO:
        to find the largest prime fraction of  600851475143
        concept -1 was n^2 , we can do 1 better 
        every prime no u see is a factor of 6 +1 or +5 i found.
        which shrinks the problem to less than n also we need to go till 
        n/2 because bigger than that cannot be a factor of the origional no 
        '''
        ai = 600851475143
        # !error is coming here but what .
        no_we_need_biggest_of = m.ceil(m.sqrt(ai))
        def isprimo(x): return any([((x-i)/6).is_integer() for i in [1, 5]])
        l = []
        for i in range(4, no_we_need_biggest_of):
            if ai % i == 0 and isprimo(i):
                l.append(i)
        # return print(l)
        for _ in l:
            if ai/_ == 1:
                return print(_)
            ai = ai/_

    def e4():
        '''
        TODO:
        2520 is the smallest number that can be
        divided by each of the numbers from 1 to 10 
        without any remainder.
        What is the smallest positive number that is evenly divisible 
        by all of the numbers from 1 to 20? 
        '''
        acc = 1
        def a(x): return all([x % i == 0 for i in range(10, 21)])
        while True:
            if a(acc) == True:
                return print(acc)
            acc += 1

    def e5(n: int) -> int:
        '''TODO : 
        A palindromic number reads the same both ways. 
        The largest palindrome made from the product of two 2-digit numbers is 
        9009 = 91 × 99.
        Find the largest palindrome made from the 
        product of two 3-digit numbers.
        as we can see a palindrome product is something like for eg 
        9009 ---> 90 --> 100-1=99  and then what i see is  91 which is like 
        N = str(no)[0]
        A = no-1
        palindromehalf = 1000/A * int(N)  - int(N)
        now this is true for like upto 400 and beyond  , for 400  
        its kinda moot but i think for like that is the point where 2 fractions converge soo 
        '''
        N = str(n)[0]
        a = n-1
        palindromehalf = int(n/a)*int(N) - int(n)
        return print(palindromehalf)

    # def e6():
        return print(assasin(10))

    def e7():
        pass

    def e8():
        pass

    def e9():
        pass

    def e10():
        pass

    def e11():
        pass

    def e12():
        pass

# !  ..................................................................................



# ? ......................USED functiona........................................................
def assasin(x):
    assasin_list = [2, 3, 5, 7, 11, 13, 17, 19]
    l = []
    if x in assasin_list:
        l.append(x)
        return l
    i = 0
    while x != 1:
        if x % assasin_list[i] == 0:
            l.append(assasin_list[i])
            x = x/assasin_list[i]
    else:
        i += 1
    return l

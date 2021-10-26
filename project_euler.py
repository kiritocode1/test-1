
import math as m
from typing import Counter
import itertools as shit
from itertools import permutations
import operator
# ? ......................USED functiona........................................................
def assasin_for_e6(x):
    '''this is so we can get a concise list of all the prime factors of the no in a list
    easy to follow , we get all the prime nos lesser than the no .
    so basically helping us to get , the primes. 
    10 ---> [2,5]
    11---> [11] because its a prime 
    20 ---> [2,5]
    25 ---> [5,5]
    etc.
    '''
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
def assak(stin):
    mid = len(stin)//2
    if len(stin)%2!=0:
        a =list(stin)
        a.pop(mid)
        stin2 = "".join(a)
        return assak(stin2)
    if len(stin)%2==0 and stin[:mid]==stin[mid:][::-1]:
        return True
# *..............................main Arcadia...................................................................
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

    def e3()->int:
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
            if ai % i == 0 and isprimo(i) and (i/25)%25!=0:
                l.append(i)
        # return print(l)
        for _ in l:
            if ai/_ == 1:
                return print(_)
            ai = ai/_

    def e6()->list:
        '''
        TODO:
        2520 is the smallest number that can be
        divided by each of the numbers from 1 to 10 
        without any remainder.
        What is the smallest positive number that is evenly divisible 
        by all of the numbers from 1 to 20? 
        '''
        l = []
        a = 1
        for i in range(1,21):
            r = []
            for j in assasin_for_e6(i):
                if j in l:
                    l.remove(j)
                    r.append(j)
                else: l.append(j)
            l = l+r
        return [i for i in shit.accumulate(l,operator.mul)][-1]
    def e5() -> str:
        '''TODO : 
        A palindromic number reads the same both ways. 
        The largest palindrome made from the product of two 2-digit numbers is 
        9009 = 91 × 99.
        Find the largest palindrome made from the 
        product of two 3-digit numbers.
        we could bruteforce this shit  .
        '''
        a = list(permutations(range(100,999),2))
        a.sort(key=lambda x : x[0]*x[1])
        a = a[::-1]
        for i in a:
            done = str(i[0]*i[1])
            if assak(done):
                return done
    def e4():
        pass
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
    
#! .................................trial  room..........................................
a = project_euler
print(a.e6())


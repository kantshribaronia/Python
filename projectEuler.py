# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:13:35 2019

@author: Kantshri
"""

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def primefact(number):
    prime =[]
    i=2
    while i*i <= number:
        if number%i:
            i=i+1
        else:
            number//=i
            prime.append(i)
    prime.append(number)
    print(max(prime))


primefact(600851475143)


-------------------------------------------------------------------------------
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def palinCheck():
    palin = []
    for i in range(100,1000):        
        for j in range(100,1000):
            #print('hi')
            number = i*j
            #print(number)
            if isPalindrome(number):
                palin.append(number)
    print(max(palin))

def isPalindrome(a):
    num = a
    #print(num)
    rev=0
    while a>0:
        last = a%10
        rev = (rev*10) + last
        a //= 10
        #print(rev)
    if num == rev:
        #print(num)
        return 1
    else:
        return 0

palinCheck()
#isPalindrome(9009)

-------------------------------------------------------------------------------
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 
def func(number):
    while number<9999999999:
        number+=1
        #print('above for loop with number=', number)
        for i in range(2,21):
            #print('Continuing for loop with i=', i)
            if(i==20):
                print(number)
                return;                
            if(number%i!=0):
                break;
    else:
        return 0;


func(2)


-------------------------------------------------------------------------------

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.













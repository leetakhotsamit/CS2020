##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 02, Question 4
##===============================================

## Question 4

import math
import check
       
def is_prime(a,b):
    '''
    is_prime_num(a,b) returns True if a is the prime number and 
    False if a is not the prime number 
    
    is_prime: Int Int => Bool
    
    requires: both a and b are positive integers
    
    Examples: 
    is_prime(5,2) => True
    is_prime(6,2) => False
    '''
    if a == 1:
        return False
    elif a == b:
        return True
    elif a%b != 0:
        return is_prime(a, b-1)
    else:
        return False
    
## Test
check.expect("Q4T1", is_prime(9,2), False)
check.expect("Q4T2", is_prime(1,2), False)
check.expect("Q4T3", is_prime(2,2), True)
       
def is_prime_divisor(c, d):
    '''
    Returns the number of prime divisors from a range of 2 to d. 
    
    is_prime_divisor: Int Int => Nat
    
    requires:
    * c and d are both positive integers
    * to be a divisor then c%d == 0
    
    Examples: 
    is_prime_divisor(12, 12) => 2
    is_prime_divisor(31, 31) => 1
    '''
    if d < 2:
           return 0 
    if (d == 2) and (c % d == 0):
           return 1       
    if (c % d == 0) and is_prime(c,d):
           return 1 + is_prime_divisor(c, d-1)     
    else:
           return is_prime_divisor(c, d-1) 

## Test
check.expect("Q4T4",is_prime_divisor(18, 18),2) 
check.expect("Q4T5",is_prime_divisor(97,97),1)

def count_prime_divisors(n):
    '''
    Returns the number of prime divisors given a positive integer n
    
    count_prime_divisors(n): Int => Nat
    
    requires: 
    * n is a positive integer
    
    Example
    count_prime_divisors (12) => 2
    '''
    return is_prime_divisor(n, n)


## Test1: below 2
check.expect("Q4T6",count_prime_divisors(1),0)
check.expect("Q4T7",count_prime_divisors(0),0)
## Test2: count only prime
check.expect("Q4T8",count_prime_divisors(2),1)
check.expect("Q4T9",count_prime_divisors(97),1)
check.expect("Q4T10",count_prime_divisors(43),1)
## Test3: count prime divisor
check.expect("Q4T11",count_prime_divisors(16),2)
check.expect("Q4T12",count_prime_divisors(90),2)
check.expect("Q4T13",count_prime_divisors(42),2)
check.expect("Q4T14",count_prime_divisors(75),1)

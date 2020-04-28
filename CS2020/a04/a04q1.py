###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 04 Question 1
### ***************************************************
###

import math
import check

def factors(n):
    '''
    Consumes a positive integer n and returns a list containing the factors of
    n
    
    factors: Nat -> (listof Nat)
    
    requires:
    * positive integers
    
    Examples:
    factors(0) -> []
    factors(12) -> [1, 2, 3, 4, 6, 12]
    factors(9) ->[1, 3, 9]
    '''
    factors_filter = lambda x: n % x == 0
    return list(filter(factors_filter, range(1,n + 1)))

## Examples
check.expect("Q1E1", factors(0), [])
check.expect("Q1E2", factors(12), [1, 2, 3, 4, 6, 12])
check.expect("Q1E3", factors(3), [1, 3])

## Test
check.expect("Q1T1", factors(10), [1, 2, 5, 10])
check.expect("Q1T2", factors(25), [1, 5, 25])
check.expect("Q1T3", factors(33), [1, 3, 11, 33])

## Checking prime numbers
check.expect("Q1T3", factors(47), [1,47])
check.expect("Q1T4", factors(97), [1,97])
check.expect("Q1T5", factors(101), [1,101])
check.expect("Q1T6", factors(1), [1])
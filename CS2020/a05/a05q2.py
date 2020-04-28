###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 05 Question 02
### ***************************************************
###

import check

def is_prime(a,b):
    '''
    is_prime_num(a,b) returns True if a is the prime number and 
    False if a is not the prime number. A prime number (a) can only be divisible 
    by 1 and itself. When a = b then there is no number in the range divisible
    by n (which means itsprime). If a is  divisible by b then it is False.
    
    
    is_prime: Nat Nat -> Bool
    
    requires: both a and b are positive integers
    
    Examples: 
    is_prime(5,2) => True
    is_prime(6,2) => False
    '''
    if a == 1:
        return False
    elif a == b:
        return True
    elif a%b == 0:
        return False
    else:
        return is_prime(a, b+1)

# Test
check.expect("Q2T1", is_prime(9,2), False)
check.expect("Q2T2", is_prime(1,2), False)
check.expect("Q2T3", is_prime(2,2), True) 

def next_prime(current_num):
    '''
    Takes into account what the current number which can either be be a prime 
    number or not. If the current number is a prime nummber, then it returns the 
    same number. If it is not a prime number, then the next prime number is 
    returned. 
    
    next_prime: Nat -> Nat
    
    examples:
    next_prime(1) -> 2
    next_prime(7) -> 7
    '''
    if is_prime(current_num,2):
        return current_num
    return next_prime(current_num + 1)

# Test 
check.expect("Q2T4", next_prime(1), 2)
check.expect("Q2T5", next_prime(7), 7)

print(next_prime(9))

def factor_acc(factors_lst, num):
    '''
    Consumes a factors list, the value for index i of factors is the nummber of 
    factors of the ith prime number. To unfactorize, the factors will be put to
    the power with respect to the prime number, this process is aplied to the 
    rest of the factors. The products are then multiplied with eachother. Num 
    is the value found at index 0. 
    
    factor_acc: (listof Nat) Nat -> Nat
    
    examples:
    factor_acc([2,0,1], 2) -> 20
    '''
    if factors_lst == []:
        return 1
    else:
        n_prime = next_prime(num)
        return n_prime**factors_lst[0] * factor_acc(factors_lst[1:], n_prime+1)
    
check.expect("Q2T6", factor_acc([2,0,1], 2), 20)

def unfactorize(factors):
    '''
    Consumes a factors list, the value for index i of factors is the nummber of 
    factors of the ith prime number. To unfactorize, the factors will be put to
    the power with respect to the prime number, this process is aplied to the 
    rest of the factors. The products are then multiplied with eachother.
    
    required: positive Nat numbers
    
    unfactorize: (listof Nat) -> Nat
    
    examples: 
    unfactorize ([]) -> 1
    nfactorize ([0]) -> 1
    unfactorize([2,0,1]) -> 20
    unfactorize([0,1,2,0,0,0,0,0,1]) -> 1725
    '''    
    if factors == []:
        return 1
    return factor_acc(factors, factors[0])

# Example
check.expect("Q2E1", unfactorize([2,0,1]), 20)
check.expect("Q2E2", unfactorize([2,1]), 12)
check.expect("Q2E3", unfactorize([0,1,2,0,0,0,0,0,1]), 1725)
check.expect("Q2E4", unfactorize([]), 1)
check.expect("Q2E5", unfactorize([1,1,0,0]), 6)

# Test
# all zeros
check.expect("Q2T7", unfactorize([0,0,0,0,0]), 1)
# all ones
check.expect("Q2T8", unfactorize([1,1,1,1]), 210)
# starting with zeros
check.expect("Q2T9", unfactorize([0,0,1,1]), 35)
# only one number present
check.expect("Q2T10", unfactorize([1]), 2)
# only one number present rest are zeros
check.expect("Q2T11", unfactorize([0,0,0,1,0,0,0]), 7)
# zero
check.expect("Q2T12", unfactorize([0]), 1)
# 10 digits
check.expect("Q2T13",unfactorize([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),6469693230)
# one number at the end
check.expect("Q2T13",unfactorize([0,0,0,0,1]),11)
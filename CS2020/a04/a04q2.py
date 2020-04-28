###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 04 Question 2
### ***************************************************
###
import check
import math 

def increasing(L):
    '''
    Consumes a non-empty list of integers (L) and returns True if the integers 
    are in strictly ascending order, where the integer in the list is less than 
    all elements that occur after it
    
    increasing: (listof Int) -> Bool
    
    requires:
    * the list (L) cannot be empty; not a non-empty list
    * the list is restrictively increasing
    
    Example:
    increasing[0] -> True
    increasing([-3, 2, 4, 8, 11]) -> True
    increasing([1,1]) -> False
    increasing([4,6,5]) -> False
    '''
    lon = list(map(lambda i: L[i+1] > L[i], range(len(L) -1)))
    if False in lon:
        return False
    else:
        return True

## Examples
check.expect("Q2E1", increasing([-3, 2, 4, 8, 11]), True)
check.expect("Q2E2", increasing([4, 6, 5]), False)
check.expect("Q2E3", increasing([2,2]), False)

## Tests
check.expect("Q2T1", increasing([-3, -4, 4, 8, 11]), False)
check.expect("Q2T2", increasing([0]), True)
check.expect("Q2T3", increasing([1,2,1]), False)
check.expect("Q2T4", increasing([5,4,3,2,1]), False)
check.expect("Q2T5", increasing([-5,4,33,200,1000]), True)
check.expect("Q2T6", increasing([-5,-4,-3,-2,-1]), True)
check.expect("Q2T6", increasing([-5,-4,-3,-2,-1]), True)
check.expect("Q2T7", increasing([-1,-1]), False)
check.expect("Q2T8", increasing([1]), True)
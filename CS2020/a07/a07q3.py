###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 07 Question 3
### ***************************************************
###
###
import check

def find_balance(L):
    '''
    Consumes a list of integers (L), and returns a new list of natural numbers 
    the same length as L. The new list returned describes the length of the 
    longest sublists within L that sum to 0.
    
    find_balance: (listof Int) -> (listof Nat)
    
    examples
    find_balance([0, 2, -8, 7, -7, 1, 7]) -> [1, 0, 5, 2, 0, 0, 0]
    find_balance([0, 0, 0]) -> [3, 2, 1]
    find_balance([-4, -5, 3, 6, -2, 6, -4, -2, 2]) ->
                 [9, 0, 0, 0, 5, 3, 0, 2, 0]
    find_balance([0]) -> [1]
    '''
    M = []
    for i in range(len(L)):
        summation = 0
        length = 0
        for j in range(i,len(L)):
            summation = summation + L[j]
            if summation == 0:  
                if (length < j - i + 1):
                    length = j - i + 1
        M.append(length)
    return M

# Examples

L= [0,0,0]
check.expect('Q3E1', find_balance(L),[3,2,1])

L= [-4,-5,3,6,-2,6,-4,-2,2]
check.expect('Q3E2', find_balance(L), [9, 0, 0, 0, 5, 3, 0, 2, 0])

L= [0,2,-8,7,-7,1,7]
check.expect('Q3E3', find_balance(L), [1, 0, 5, 2, 0, 0, 0])

# Test
# one zero
L = [0]
check.expect('Q3T1', find_balance(L), [1])

#  negative and positive of numbers
L = [-3,-2,-1,0,1,2,3]
check.expect('Q3T2', find_balance(L), [7, 5, 3, 1, 0, 0, 0])

#  0 at the end
L = [1,2,3,4,5,6,7,8,9,0]
check.expect('Q3T3', find_balance(L), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

# 0 in the beginning of list
L = [0,1,2,3,4,5,6,7,8,9]
check.expect('Q3T4', find_balance(L), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# modifying E2
L= [-4,-5,3,6,-2,6,-6,-2,2]
check.expect('Q3T5', find_balance(L), [4, 7, 0, 0, 0, 4, 0, 2, 0])

# all 0 
L = [0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0]
check.expect('Q3T6', find_balance(L), 
             [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# all negative
L = [-1,-2,-3,-4,-5]
check.expect('Q3T7', find_balance(L), [0,0,0,0,0])



###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 06 Question 3
### ***************************************************
###
###

import check

def bernoulli_triangle(n):
    '''
    Consumes a positive integer n and returns a list of length n, where the 
    first element is a list representing the first row of Bernoulli's Triangle
    and so on. A list of list is created.
    
    bernoulli_triangle: Nat -> (listof (listof Nat))
    
    requires:
    * n is Nat (positive)
    
    example
    bernoulli_triangle(1) -> [[1]]
    bernoulli_triangle(0) -> [[1]]
    bernoulli_triangle(4) -> [[1], [1, 2], [1, 3, 4], [1, 4, 7, 8]]
    '''
    L = [[1]]
    for i in range(1,n):
        row = [1]
        for j in range(1,i):
            row.append(L[i-1][j]+L[i-1][j-1])
        row.append(L[i-1][-1]*2)
        L.append(row)
    return L

# Example
check.expect('Q3E1', bernoulli_triangle(1),[[1]])
check.expect('Q3E2', bernoulli_triangle(4),[[1],
                                            [1, 2], [1, 3, 4], [1, 4, 7, 8]])

# Test
# triangle up to the 10th row
check.expect('Q3T1',
             bernoulli_triangle(10),
             [[1],
              [1, 2],
              [1, 3, 4],
              [1, 4, 7, 8],
              [1, 5, 11, 15, 16],
              [1, 6, 16, 26, 31, 32],
              [1, 7, 22, 42, 57, 63, 64],
              [1, 8, 29, 64, 99, 120, 127, 128],
              [1, 9, 37, 93, 163, 219, 247, 255, 256],
              [1, 10, 46, 130, 256, 382, 466, 502, 511, 512]])
# first row
check.expect('Q3T2', bernoulli_triangle(2),
             [[1],
              [1, 2]])
# third row
check.expect('Q3T3', bernoulli_triangle(3),
             [[1],
              [1, 2],
              [1, 3, 4]])

# row 0 
check.expect('Q3T4', bernoulli_triangle(0),
             [[1]])
# row 6
check.expect('Q3T5', bernoulli_triangle(6),
             [[1],
              [1, 2],
              [1, 3, 4],
              [1, 4, 7, 8],
              [1, 5, 11, 15, 16],
              [1, 6, 16, 26, 31, 32]])             
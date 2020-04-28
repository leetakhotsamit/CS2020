### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 05 Question 03
### ***************************************************
###

import check

def build_row(n,row):
  '''
  Build row consumes n, which is the number of components in the list from 0 to
  n. Rows is in respect to the row found in the matrix. So building a matrix of 
  3, in row 1, the list contains [0,1,2,3].
  
  build_row: Nat Nat -> (listof Nat)
  
  requires:
  * n and row cannot be empty
  
  examples:
  build_row(3,1) -> [0,1,2,3]
  build_row(3,2) -> [0,2,4,6]
  '''
  if n == 0:
    return [0]
  else:
    return build_row(n-1,row) + [(row*n)]

# Test
check.expect("Q3T1", build_row(3,1), [0,1,2,3])
check.expect("Q3T2", build_row(3,2), [0,2,4,6])

def build_matrix(n,row):
  '''
  Build matrix consumes n, which is the size , (n+1)x(n+1).The matrix is 
  composed of four lists because the first list is a list of zero. The row 
  represent the amount of row to build up to. 
  
  build_matrix: Nat Nat -> (listof (listof Nat))
  
  requires:
  * n and row are Nat or 0
  
  examples:
  build_matrix(3,2) -> [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
  build_matrix(3,0) -> [[0, 0, 0, 0]
  '''
  if row == 0:
    return [build_row(n,0)]
  else:
    return build_matrix(n,row-1) + [build_row(n,row)]

# Test
check.expect("Q3T3", build_matrix(3,0), [[0, 0, 0, 0]])
check.expect("Q3T4", build_matrix(3,2), [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]])

def times_table(n):
  '''
  Consumes a natural number n and returns a times table for all numbers betweeen
  0 and n inclusive. A times table T is a list of lists, of size (n+1)x(n+1)
  
  times_table: Nat -> (listof (listof Nat))
  
  requires:
  * n is a Nat or 0
  
  examples
  times_table (0) -> [[0]]
  times_table(3) -> [[0, 0, 0, 0],[0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]
  '''
  return build_matrix(n,n)

# Example
check.expect("Q3E1", times_table (0),[[0]])
check.expect("Q3E2", times_table(3),[[0, 0, 0, 0],
                                     [0, 1, 2, 3],
                                     [0, 2, 4, 6], 
                                     [0, 3, 6, 9]])

# Test
check.expect("Q3T5", times_table(2), [[0, 0, 0],
                                      [0, 1, 2],
                                      [0, 2, 4]])
check.expect("Q3T6", times_table(5),[[0, 0, 0, 0, 0, 0],
                                     [0, 1, 2, 3, 4, 5],
                                     [0, 2, 4, 6, 8, 10],
                                     [0, 3, 6, 9, 12, 15],
                                     [0, 4, 8, 12, 16, 20],
                                     [0, 5, 10, 15, 20, 25]])
check.expect("Q3T7", times_table(1), [[0, 0],
                                      [0, 1]])
check.expect("Q3T8", times_table(4), [[0, 0, 0, 0, 0],
                                      [0, 1, 2, 3, 4],
                                      [0, 2, 4, 6, 8],
                                      [0, 3, 6, 9, 12],
                                      [0, 4, 8, 12, 16]])


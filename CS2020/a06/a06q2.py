###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 06 Question 2
### ***************************************************
###
###

import check

def digital_root_add(n):
  '''
  Consumes an int (n) and adds all the numbers until the result returns a single
  digit number (digital root)
  
  requires:
  * n is positive or 0
  
  digital_root_add: Nat -> Nat
  
  Examples:
  digital_root_add(98) -> 8
  digital_root_add(0) -> 0
  digital_root_add(100) -> 1
  digital_root_add(12345) -> 6
  '''
  while True:
    x=list(str(n))
    if len(x)==1:
      return n
    else:
      n=0
      for i in x:
        n+=int(i)

# Test        
check.expect('Q2T1', digital_root_add(98),8)
check.expect('Q2T2', digital_root_add(0),0)
check.expect('Q2T3', digital_root_add(100),1)
check.expect('Q2T4', digital_root_add(12345), 6)

def mutate_list(L, i):
  '''
  consumes a list (L) and an integer for the index (i). Returns a mutated list
  by replacing the Int in the list with the product of digital_root_add(n) with
  respect to the index.
  
  effects: mutates the list (L)
  
  mutate_list: (listof Int) Nat -> None
  
  examples
  mutate = [0, 22, 100, 98, 12345]
  mutate_list(mutate,3) -> None
   and the list is mutated to [0, 22, 100, 8, 6]
  '''
  if len(L) == i:
    return None
  else:
    L[i] = digital_root_add(L[i])
    return mutate_list(L, i + 1)
# Test
mutate = [0, 22, 100, 98, 12345]
check.expect('Q2T5', mutate_list(mutate,3), None)
check.expect('Q2T5: mutate', mutate,[0, 22, 100, 8, 6])

def digital_roots(L):
  '''
  Consumes a list (L) and mutates the list by repetedly adding all the digits 
  of the number and continues until the result is a single digit.
  
  effects: mutates the list (L)
  
  digital_roots: (listof Nat) -> None
  
  requires: 
  * integers in list (L) are positive
  
  examples
  L1 = [1]
  L2 = [0, 22, 100, 98, 12345]
  L3 = []
  L4 = [0]
  digital_roots(L1) -> None 
    and L1 is mutated to [1]
  digital_roots(L2) => None
    and L2 is mutated to [0,4,1,8.6]
  digital_roots(L3) -> None 
    and L3 is mutated to []
  digital_roots(L4) -> None 
    and L4 is mutated to [0]
  '''
  return mutate_list(L, 0)

# Example 
L1 = [1]
L2 = [0, 22, 100, 98, 12345]
L3 = []
L4 = [0]

# one element in list
check.expect('Q2E1', digital_roots(L1), None)
check.expect('Q2E1: mutate', L1, [1])
# 5 elements in list
check.expect('Q2E2', digital_roots(L2), None)
check.expect('Q2E2: mutate', L2, [0, 4, 1, 8, 6])
# empty
check.expect('Q2E3', digital_roots(L3), None)
check.expect('Q2E3: mutate', L3, [])
# zero as the only element in list
check.expect('Q2E4', digital_roots(L4), None)
check.expect('Q2E4: mutate', L4, [0])

# Test
L5 = [123,456,789,95,227,349,567,234,87,99,87,988]
L6 = [0,0,0,0,98]
L7 = [1,2,3,4,5,6,7,8,9,10]
L8 = [111,111,111,111,111]
L9 = [0,0,0,0,0]
L10 = [98,0,0,0,0]
# 10 items in a list, adding iteration needs to happen more than once
check.expect('Q2T6', digital_roots(L5), None)
check.expect('Q2T6: mutate', L5, [6, 6, 6, 5, 2, 7, 9, 9, 6, 9, 6, 7])

# 10 items in a list, numbers are all single digits
check.expect('Q2T7', digital_roots(L5), None)
check.expect('Q2T7: mutate', L5, [6, 6, 6, 5, 2, 7, 9, 9, 6, 9, 6, 7])

# zeros and one digital root at end
check.expect('Q2T8', digital_roots(L6), None)
check.expect('Q2T8: mutate', L6, [0, 0, 0, 0, 8])

# numbers up to 10
check.expect('Q2T9', digital_roots(L7), None)
check.expect('Q2T9: mutate', L7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1])

# mutates list with all the same numbers
check.expect('Q2T10', digital_roots(L8), None)
check.expect('Q2T10: mutate', L8, [3, 3, 3, 3, 3])

# mutating list of 0
check.expect('Q2T11', digital_roots(L9), None)
check.expect('Q2T11: mutate', L9, [0,0,0,0,0])

# digital root first on list
check.expect('Q2T12', digital_roots(L10), None)
check.expect('Q2T12: mutate', L10, [8,0,0,0,0])


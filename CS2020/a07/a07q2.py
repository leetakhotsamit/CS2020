###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 07 Question 2
### ***************************************************
###
###

import check

def merge(lst,start,pos,end):
    '''
    Merge consume a list (lst) starting index (start), current position index
    (pos) and an end index (end). The integer at the current position (pos) 
    will be sorted into place with respect to the integers in the list already.
    place.The function mutates the list and returns None.
    
    Effects: mutates the list (lst)
    
    merge: (listof Int) Nat Nat Nat -> None
    
    examples:
    L = [0,3,1,29,8,2,9]
    merge(L,0,5,len(L)) -> None
      and mutates the list to [0, 2, 3, 1, 9, 29, 8]
      Note: 2 found at pos 5 is greater than 0, so it will be placed after 0
      
    L = [1,-1,2,-2,3,-3]
     merge(L,0,5,len(L)) -> None
      and mutates the list to [-3, 1, -1, 2, -2, 3]
      Note: -3 found at pos 5 is less than 1, so it will be placed before 1
    
    '''
    front = lst[start:pos]
    back = lst[pos:end]
    pos1 = 0
    pos2 = 0
    for i in range(start,end):
        if pos2 >= len(back) or (pos1 < len(front) and front[pos1] < back[pos2]):
            lst[i] = front[pos1]
            pos1 = pos1 + 1
        else:
            lst[i] = back[pos2]
            pos2 = pos2 + 1  

# Test
L = [0,3,1,29,8,2,9]
check.expect('Q2T1', merge(L,0,5,len(L)), None)
check.expect('Q2T1: mutate', L, [0, 2, 3, 1, 9, 29, 8])

L = [1,-1,2,-2,3,-3]
check.expect('Q2T2', merge(L,0,5,len(L)), None)
check.expect('Q2T2: mutate', L, [-3, 1, -1, 2, -2, 3])

def mergeSort(L,start,end):
    '''
    Consumes a list (L), the starting index (start), and the end index (end).
    This is a divide and conquer algorithm, where the list is divided into two.
    The function sorts the first half, and sorts the second half.  This function
    returns None, but mutates the list by combining the sorted first and second
    half.
    
    Effects: mutates the list (L)
    
    mergeSort: (listof Int) Nat Nat -> None
    
    examples:
    L = [0,3,1,29,8,2,9]
      merge(L,0,5,len(L)) -> None
      and mutates the list to [0,1,2,3,8,9,29]
      Note: 2 found at pos 5 is greater than 0, so it will be placed after 0
      
    L = [1,-1,2,-2,3,-3]
     merge(L,0,5,len(L)) -> None
      and mutates the list to [-3,-2,-1,1,2,3]
      Note: -3 found at pos 5 is less than 1, so it will be placed before 1
    '''
    if end - start > 1:
        mid = int((start+end)//2)
        mergeSort(L,start,mid)
        mergeSort(L,mid,end)
        merge(L,start,mid,end)

# Test
L = [0,3,1,29,8,2,9]
check.expect('Q2T3', mergeSort(L,0,len(L)), None)
check.expect('Q2T3: mutate', L, [0,1,2,3,8,9,29])

L = [1,-1,2,-2,3,-3]
check.expect('Q2T4', mergeSort(L,0,len(L)), None)
check.expect('Q2T4: mutate', L, [-3,-2,-1,1,2,3])

def binarysearch(L, target):
    '''
    Consumes a value index list (L). The list (L) is sorted 
    based on the first value found in L. The second value in L is the index 
    where the first value is found in the original list.The target is the value
    to be searched for in the value index list, the function returns the index 
    (Nat) where the target can be found in L. If target is not found then it 
    returns -1
    
    binarysearch: (listof (listof Nat)) Nat -> Nat
    
    examples:
    OGList = [42, 0, 42, 12, 6000, 1]
    value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
    binarysearch(value_index, 12) -> 2
    
    OGList = [42, 0, 42, 12, 6000, 1]
    value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
    binarysearch(value_index, 6000) -> 5
    
    OGList = [42, 0, 42, 12, 6000, 1]
    value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
    binarysearch(value_index, 100) -> -1
    '''
    beginning = 0
    end = len(L) - 1
    lst = mergeSort(L,0,len(L))
    while beginning <= end:
        mid = (beginning + end) // 2
        if ((L[mid][0] == target) and 
            ((mid==len(L)-1) or (L[mid][0]<L[mid+1][0]))):
            return mid
        elif L[mid][0] > target:
            end = mid - 1
        else:
            beginning = mid + 1
    return -1

# Test
OGList = [42, 0, 42, 12, 6000, 1]
value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
check.expect('Q2T5', binarysearch(value_index, 12), 2)

OGList = [42, 0, 42, 12, 6000, 1]
value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
check.expect('Q2T6',binarysearch(value_index, 6000),5)

OGList = [42, 0, 42, 12, 6000, 1]
value_index = [[0, 1], [1, 5], [12, 3], [42, 0], [42, 2], [6000, 4]]
check.expect('Q2T7',binarysearch(value_index, 100),-1)
    
def no_pairs(L):
    '''
    Consumes a list of natural numbers (L), mutates the original list and 
    replaces any natural number that appears exactly twice with -1. The function
    returns None.
    
    Effects: mutates the list (L)
    
    no_pairs: (listof Nat) -> None
    
    examples:
    
    L1 = [254, 955, 198, 590, 368]
    no_pairs(L1) -> None
      and mutates the list to [254, 955, 198, 590, 368]
    
    L2 = [42, 0, 42, 12, 6000, 1]
    no_pairs(L2) -> None
      and mutates the list to [-1, 0, -1, 12, 6000, 1]
    
    L3 = [4, 4, 4, 2, 1, 2, 1]
    no_pairs(L3) -> None
      and mutates the list to [4, 4, 4, -1, -1, -1, -1]
    
    L4 = []
    no_pairs(L4) -> None
     and mutates the list to []
    '''
    # index list 
    index=[0 for x in range(len(L))]
    value_index = []
    for i in range(len(L)):
        value_index.append([L[i],i])
    # sort the value_index list
    mergeSort(value_index,0,len(value_index))
    for i in range(len(L)):
        # if L[i] is not duplicate already
        if(L[i]!=-1):
            # find index in the value_index list
            index_search = binarysearch(value_index,L[i])
            if((index_search > 0) and (index[value_index[index_search][1]]==0)):
                index[value_index[index_search][1]]=1
                if(value_index[index_search-1][1]==i):
                    L[i]= -1
                    L[value_index[index_search][1]]= -1

# Examples
L1= [254, 955, 198, 590, 368]
L2= [4,4,4,2,1,2,1]
L3= [42, 0, 42, 12, 6000, 1]

check.expect('Q2E1', no_pairs(L1), None)
check.expect('Q2E1: mutate', L1, [254, 955, 198, 590, 368])

check.expect('Q2E2', no_pairs(L2), None)
check.expect('Q2E2: mutate', L2, [4, 4, 4, -1, -1, -1, -1])

check.expect('Q2E3', no_pairs(L3), None)
check.expect('Q2E3: mutate', L3, [-1, 0, -1, 12, 6000, 1])

# Test
# only 1 number
L = [2]
check.expect('Q2T8', no_pairs(L), None)
check.expect('Q2T8: mutate', L, [2])

# zero case
L = [0]
check.expect('Q2T9', no_pairs(L), None)
check.expect('Q2T9: mutate', L, [0])

# only 2 numbers, a pair
L = [2,2]
check.expect('Q2T10', no_pairs(L), None)
check.expect('Q2T10: mutate', L, [-1,-1])

# only 2 numbers, not a pair
L = [2,100]
check.expect('Q2T11', no_pairs(L), None)
check.expect('Q2T11: mutate', L, [2,100])

# 4 number list, one pair and one not
L = [33,27,2,2]
check.expect('Q2T12', no_pairs(L), None)
check.expect('Q2T12: mutate', L, [33,27,-1,-1])

# 4 number list, same number
L = [2,2,2,2]
check.expect('Q2T13', no_pairs(L), None)
check.expect('Q2T13: mutate', L, [2,2,2,2])

# 10 numbers, 5 pairs
L = [1,1,2,2,3,3,4,4,5,5]
check.expect('Q2T14', no_pairs(L), None)
check.expect('Q2T14: mutate', L, [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

# 10 numbers, 3 pairs
L = [1,1,2,2,3,3,4,5,5,5]
check.expect('Q2T15', no_pairs(L), None)
check.expect('Q2T15: mutate', L, [-1,-1,-1,-1,-1,-1,4,5,5,5])

# 20 numbers, pair not found
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
check.expect('Q2T16', no_pairs(L), None)
check.expect('Q2T16: mutate', L,
             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# 20 numbers, pairs found in the beginning
L = [1,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
check.expect('Q2T17', no_pairs(L), None)
check.expect('Q2T17: mutate', L,
             [-1,-1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# 20 numbers, pairs found in the middle
L = [1,2,3,4,5,6,7,8,9,9,11,12,13,14,15,16,17,18,19,20]
check.expect('Q2T17', no_pairs(L), None)
check.expect('Q2T17: mutate', L,
             [1,2,3,4,5,6,7,8,-1,-1,11,12,13,14,15,16,17,18,19,20])

# 20 numbers, pairs found in the middle
L = [1,2,3,4,5,6,7,8,9,10,11,11,13,14,15,16,17,18,19,20]
check.expect('Q2T17', no_pairs(L), None)
check.expect('Q2T17: mutate', L,
             [1,2,3,4,5,6,7,8,9,10,-1,-1,13,14,15,16,17,18,19,20])

# 20 numbers, pairs found at the end
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,20]
check.expect('Q2T17', no_pairs(L), None)
check.expect('Q2T17: mutate', L,
             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,-1,-1])

# empty list 
L = []
check.expect('Q2T18', no_pairs(L), None)
check.expect('Q2T18: mutate', L,
             [])

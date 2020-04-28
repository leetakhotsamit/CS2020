###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 06 Question 1
### ***************************************************
###
###

import check

def factors(n):
    '''
    Returns a list containing the factors of num in increasing order
    
    factors: Int -> (listof Int)
    
    Examples:
    factors(1) -> [1]
    factors(3) -> [1,3]
    factors(24) -> [1,2,3,4,6,8,12,24]
    '''
    if n == 1 : return [1]
    factor = [1,n]
    i = n-1
    j = 2
    while i > j:
        if n % j == 0:
            factor.append(j)
            if j != int(n/j) : 
                factor.append(int(n/j)) 
            i = int(n/j)  
        j += 1 
    factor.sort()
    return factor  

# Examples
check.expect('one',factors(1),[1])
check.expect('a prime',factors(3),[1,3])
check.expect('composite with some prime factors',factors(24),
             [1,2,3,4,6,8,12,24])

# Test
check.expect('composite and all factors primme',factors(10),
             [1,2,5,10])
check.expect('square of a prime',factors(9),[1,3,9])
check.expect('at least 10 factors',factors(120),
             [1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120])


def new_word(s):
    '''
    Returns new string where each instance of s[2], not including s[2] itself, 
    is changed with a '#' symbol
    
    new_word: Str -> Str
    
    Examples:
    
    '''
    if len(s) < 3:
        return s    
    else:
        third_letter = s[2]
        word_lst = []
    for letter in s:   
        if letter == third_letter:
            letter = '#'
        word_lst.append(letter)
        new_string = ''.join(word_lst)
        keep_third = new_string[0:2] + third_letter + new_string[3:]
    return keep_third  

# Examples    
check.expect('empty', new_word(''),'')
check.expect('short', new_word('me'), 'me')
check.expect('full', new_word('bubble'),'#ub#le')

# Test
check.expect('single letter', new_word('a'),'a')
check.expect('3 letters no repeat', new_word('abc'),'abc')
check.expect('3 letters with repeat', new_word('aba'),'#ba')
check.expect('longer string, no repeat', new_word('norepeat'),'norepeat')
check.expect('longer string, repeat', new_word('mmccalister'),'m#calister')
check.expect('longer string, repeat after', new_word('awesome'),'awesom#')
check.expect('char3 in the wrong case', new_word('awEsome'),'awEsome')
check.expect('all same', new_word('a'*100),'##' + 'a' + '#'*97)
check.expect('all #', new_word('#'*57), '#'*57)
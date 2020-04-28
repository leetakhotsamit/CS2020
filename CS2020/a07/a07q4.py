###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 07 Question 4
### ***************************************************
###
###

import check

def string_clean(s):
    '''
    Consues a string (s) and returns a string. The string should be similar 
    to the original string, but for every digit that appears in the string, a 
    number of characters correspoding to the string should be removed fromm 
    the returned string. 
    
    string_clean: Str -> Str
    
    examples:
    string_clean("") -> ""
    string_clean("I love CS116!*!*!?") -> "I love CS?"
    string_clean("6Hello") -> ""
    string_clean("I have 0 apples and 39 pears") -> "I have 0 apples and pears"
    '''
    string_list = []
    prev_index = 0
    index = 0
    while index < len(s):
        if s[index].isdigit() and s[index] != '0':
            string_list.append(s[prev_index:index])
            index += int(s[index])
            prev_index = index  
        elif s[index] == '0':
            string_list.append(s[prev_index:index + 1])
            index += 1
            prev_index = index 
        else:
            index += 1
    string_list.append(s[prev_index:index])
    return ("".join(string_list))

# Examples
check.expect('Q4E1', string_clean(""), '')
check.expect('Q4T2', string_clean("I love CS116!*!*!?"), 'I love CS?')
check.expect('Q4T3', string_clean("6Hello"), '')
check.expect('Q4T4', string_clean("29Hello!"), 'Hello!')
check.expect('Q4T5', string_clean("car4pent3ers"), 'carts')
check.expect('Q4T6', string_clean("I have 0 apples and 39 pears"), 
             'I have 0 apples and pears')

# Test
# string with 0 in the beginning
check.expect('Q4T1', string_clean('0hello'), '0hello')

# string with 0 at the end
check.expect('Q4T2', string_clean('hello0'), 'hello0')

# removine 1 character (the number)
check.expect('Q4T3', string_clean('1hello'), 'hello')

# removing 2 characters (number + char)
check.expect('Q4T4', string_clean('2hello'), 'ello')

check.expect('Q4T5', string_clean("I have 39 apples and 0 pears"), 
             'I have apples and 0 pears')

check.expect('Q4T6', string_clean("I have 9 apples,0 pears"), 
             'I have 0 pears')

# removing spaces
check.expect('Q4T7', string_clean("3        "), 
             '      ')

#removing numbers
check.expect('Q4T8', string_clean("123456789"), 
             '')

# removing non-alpha
check.expect('Q4T9', string_clean("12!@#$%^&*"), 
             '@#$%^&*')

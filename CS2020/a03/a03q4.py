##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 03, Question 4
##===============================================
import check 

## Question 4

def check_upper(s):
    '''
    Consumes a string containing alphanumeric characters and/or 
    non-numeric characters if any and returns a string containing only 
    upper characters
    
    check_upper: Str -> Str
    
    Example:
    check_upper("dkjsfhDdfj") -> "D"
    check_upper("Hello World!") ->"HW"
    '''
    if len(s) == 0:
        return ''
    if s[0].isupper():
        return s[0] + check_upper(s[1:])
    else:
        return check_upper(s[1:])
    
## Contains uppercase    
check.expect("Q4T1:",check_upper("dkjsfhDdfj"),"D")

## No uppercase
check.expect("Q4T2:",check_upper("hello world!"),"")

def count_upper(s):
    '''
    Returns a count of 1 if there is at least 1 uppercase character 
    in a string and a count of 0 if there are no uppercase characters
    
    count_upper: Str -> Str
    
    Examples:
    count_upper("dkjsfhDdfj") -> 1
    count_upper("hello world!") -> 0
    '''
    count = 0
    if len(check_upper(s)) >= 1:
        return count + 1
    else: 
        return count + 0

## Has an uppercase: score is 1
check.expect("Q4T3:",count_upper("dkjsfhDdfj"), 1)

## Does not have an uppercase: score is 0
check.expect("Q4T4:",count_upper("hello world!"), 0)

def check_lower(s):
    '''
    Consumes a string containing alphanumeric characters and/or 
    non-numeric characters if any and returns a string containing only 
    lower characters
    
    check_lower: Str -> Str
    
    Example:
    check_lower("dkjsfhDdfj") -> "dkjsfhdfj"
    check_lower("hello world!") ->"elloorld"
    '''
    if len(s) == 0:
        return ''
    if s[0].islower():
        return s[0] + check_lower(s[1:])
    else:
        return check_lower(s[1:])

## Contains lower case
check.expect("Q4T5:",check_lower("dkjsfhDdfj"),"dkjsfhdfj")

## No lowercase 
check.expect("Q4T6:",check_lower("HELLOWORLD!"),"")

def count_lower(s):
    '''
    Returns a count of 1 if there is at least 1 lowercase character 
    in a string and a count of 0 if there are no lowercase characters
    
    count_upper: Str -> Str
    
    Examples:
    count_lower("dkjsfhDdfj") -> 1
    count_lower("HELLO WORLD!") -> 0
    '''
    count = 0
    if len(check_lower(s)) >= 1:
        return count + 1
    else: 
        return count + 0

## Has a lowercase char: score is 1    
check.expect("Q4T7:",count_lower("dkjsfhDdfj"),1)

## Does not have a lowercase char: score is 0
check.expect("Q4T8:",count_lower("HELLO WORLD"),0)

def check_not_alnum(s):
    '''
    Consumes a string containing alphanumeric characters and/or 
    non-numeric characters if any and returns a string containing non alpha-
    numeric characters
    
    check_not_alnum: Str -> Str
    
    Example:
    check_not_alnum("dkjsfhDdfj_;df#") -> "_;#"
    check_not_alnum("Hello World!") ->"!"
    '''    
    if len(s) == 0:
        return ''
    if not s[0].isalnum():
        return s[0] + check_not_alnum(s[1:])
    else:
        return check_not_alnum(s[1:])

## Contains alphanum char
check.expect("Q4T9:",check_not_alnum("dkjsfhDdfj_;df#"),"_;#")

## No alphanum char
check.expect("Q4T10:",check_not_alnum("HelloWorld"),"")

def count_not_alnum(s):
    '''
    Returns a count of 1 if there is at least 3 non-alphanumeric characters 
    in a string and a count of 0 otherwise
    
    count_not_alnum: Str -> Str
    
    Examples:
    count_not_alnum("dkjsfhDdfj_;df#") -> 1
    count_not_alnum("Hello World!") -> 0
    '''    
    count = 0
    if len(check_not_alnum(s)) >= 3:
        return count + 1
    else: 
        return count + 0
    
## Contains alphanum chars >= 3: score is 1
check.expect("Q4T11:",count_not_alnum("dkjsfhDdfj_;df#"), 1)

## Contains alphanum chars less than 3: score is 1
check.expect("Q4T12:",count_not_alnum("Hello World!"), 0)

def check_num(s):
    '''
    Consumes a string containing alphanumeric characters and/or 
    non-alphanumeric characters if any and returns a string containing only numbers
    
    check_num: Str -> Str
    
    Example:
    check_num("sdk10393;df#") -> "10393"
    check_num("H3llo World!") ->"3"
    '''     
    if len(s) == 0:
        return ''
    if s[0].isnumeric():
        return s[0] + check_num(s[1:])
    else:
        return check_num(s[1:])    

## Contains numbers
check.expect("Q4T13:",check_num("sdk10393;df#"),"10393")

## Does not contain numbers
check.expect("Q4T14:",check_num("Hello World!"),"")


def count_num(s):
    '''
    Returns a count of 1 if there is at least 2 numeric characters in a string 
    and a count of 0 otherwise
    
    count_num: Str -> Str
    
    Examples:
    count_num("sdk10393;df#"),"10393" -> 1
    count_num("H3llo World!") -> 0
    '''     
    count = 0
    if len(check_num(s)) >= 2:
        return count + 1
    else: 
        return count + 0

## Contains at lease 2 numbers in string: score is 1
check.expect("Q4T15:",count_num("sdk10393;df#"),1) 

## Contains less than 2 numbers in str: score is 0
check.expect("Q4T16:",count_num("H3llo World!"),0)  

def check_space(s):
    '''
    Consumes a string containing alphanumeric characters and/or 
    non-alphanumeric characters if any and returns a string containing only spaces
    
    check_space: Str -> Str
    
    Example:
    check_space("sdk1039  3;df#") -> "  "
    check_space("HelloWorld!") -> ""
    '''         
    if len(s) == 0:
        return ''
    if s[0].isspace():
        return s[0] + check_space(s[1:])
    else:
        return check_space(s[1:])  

## Has space in string   
check.expect("Q4T17:",check_space("sdk1039  3;df#"),"  ") 

## Has no space
check.expect("Q4T18:",check_space("HelloWorld"),"") 

def count_space(s):
    '''
    Returns a count of 1 if there are no spaces in a string and a count of 0 
    if there are spaces
    
    count_num: Str -> Str
    
    Examples:
    count_space("sdk1039  3;df#") -> 0
    count_space("HelloWorld!") -> 1
    '''         
    count = 0
    if len(check_space(s)) == 0:
        return count + 1
    else: 
        return count + 0

## Contains a space: score is 0
check.expect("Q4T19:",count_space("sdk1039  3;df#"), 0)

## No spaces: score is 1
check.expect("Q4T20:",count_space("HelloWorld!"), 1)

def count_length(s):
    '''
    Returns a count of 1 if the string length is at least 10 characters and 0
    if it is not
    
    count_num: Str -> Str
    
    Examples:
    count_length("goodPass12!@@") -> 1
    count_length("weak12!") -> 0
    '''       
    count = 0 
    if len(s) >= 10:
        return count + 1
    else:
        return count + 0

## String length is >= 10: score is 1
check.expect("Q4T21:",count_length("goodPass12!@@"), 1) 

## String length is less than 10
check.expect("Q4T22:",count_length("weak12!"), 0) 

def total(s):
    '''
    Consumes an individual string and the function does a tally based on the
    following criteria and can either score 1 or 0. The following criteria are:
    * 1 point if the string has at least 10 characters
    * 1 point if the string has at least 1 uppercase character
    * 1 point if the string has at least 1 lowercase character
    * 1 point if the string has at least 3 nonalphabetic characters
    * 1 point if the string has at least 2 digits
    * 1 point if the string contains no spaces
    
    total: Str -> Nat
    
    Examples:
    total("goodPass12!@@") -> 6
    total("fairPass !!!") -> 4
    total("weak12!") -> 3
    '''
    total = (count_space(s) + count_lower(s) + count_length(s) +
             count_upper(s) + count_not_alnum(s) + count_num(s))
    return total

## Has all the criteria
check.expect("Q4T23:",total("goodPass12!@@"),6) 

## Meets 4 out of 6 of the criteria
check.expect("Q4T24:",total("fairPass !!!"),4)

## Meets 3 out of 6 of the criteria
check.expect("Q4T25:",total("weak12!"),3)


def new_password():
    '''
    Returns None and prints the strength of the password. The strength of 
    the password follows the follwing criteria:
    * 1 point if the string has at least 10 characters
    * 1 point if the string has at least 1 uppercase character
    * 1 point if the string has at least 1 lowercase character
    * 1 point if the string has at least 3 nonalphabetic characters
    * 1 point if the string has at least 2 digits
    * 1 point if the string contains no spaces
    
    Effects: Prints to screen
    
    new_password: Str -> None
    
    Requires:
    * if the password contains all the criteria, print "Good"
    * if the password contains 4-5 of the 6 criterias, print "Fair"
    * otherwise print weak
    
    Examples:
    new_password("goodPass12!@@") -> None 
    and prints "Good"
    
    new_password("fairPass !!!") -> None 
    and prints "Fair"
    
    new_password("") -> None 
    and prints "Weak"
    
    new_password("weak12!") -> None 
    and prints "Weak"
    '''
    weak_message = "Weak"
    fair_message = "Fair"
    good_message = "Good" 
    password = input("Enter password: ")
    
    if total(password) == 6:
        print(good_message)
    
    elif total(password) == 5 or total(password) == 4:
        print(fair_message)  
    
    else: 
        print(weak_message)
      

## Good case
check.set_input("goodPass12!@@")
check.set_screen("Good")
check.expect("Q4E1:", new_password(), None)

## Fair case
check.set_input("fairPass !!!")
check.set_screen("Fair")
check.expect("Q4E2:", new_password(), None)

## Weak case
check.set_input("weak12!")
check.set_screen("Weak")
check.expect("Q4E3:", new_password(), None)

## has a space, no numbers, only 1 alphanumeric
check.set_input("Hello World!")
check.set_screen("Weak")
check.expect("Q4T26:", new_password(), None)

## does not have >= 3 non alphanumeric
check.set_input("HelloWorld12!")
check.set_screen("Fair")
check.expect("Q4T27:", new_password(), None)

## one space
check.set_input(" ")
check.set_screen("Weak")
check.expect("Q4T28:", new_password(), None)

## empty case
check.set_input("")
check.set_screen("Weak")
check.expect("Q4T29:", new_password(), None)

## less than 10 char, but checks off everything else
check.set_input("!!!abC12")
check.set_screen("Fair")
check.expect("Q4T30:", new_password(), None)

## no non-alphanumeric
check.set_input("abCdEfgh412")
check.set_screen("Fair")
check.expect("Q4T31:", new_password(), None)

## no upper case
check.set_input("abcdfgh412!!!")
check.set_screen("Fair")
check.expect("Q4T32:", new_password(), None)

## no lowercase
check.set_input("!!!ABCDEFG412")
check.set_screen("Fair")
check.expect("Q4T33:", new_password(), None)

## no numbers
check.set_input("!!!ABCDEFGhijklm")
check.set_screen("Fair")
check.expect("Q4T34:", new_password(), None)







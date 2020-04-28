##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 03, Question 2
##===============================================
import check

## Question 2

def removal(s):
    '''
    Returns the lower case form the the string with the removal of spaces, 
    non alphabetic characters and numbers
    
    removal: Str -> None
    
    requires:
    * all non-alnum to be removed
    * space to be removed
    * string is in lower case
    * numbers are removed
    
    Examples:
    removal("moM") -> None
    and prints "mom"
    
    removal("computers") -> None
    and prints "computers"
    '''
    s = s.lower()
    if len(s) == 0:
        return "" 
    elif not s[0].isalnum():
        return "" + removal(s[1:])
    elif s[0].isalpha():
        return s[0] + removal(s[1:])
    elif s[0].isdigit():
        return "" + removal(s[1:])
    else:
        return removal(s[1:])

## Upper and Lower Char
check.set_print_exact("mom")
check.expect("Q2T1:", print(removal("moM")), None)

## Not palindrome
check.set_print_exact("computers")
check.expect("Q2T2:", print(removal("computers")), None)

def reversal(s):
    '''
    Consumes a string and returns the string in reverse 
    
    reversal: Str -> Str
    
    Requires:
    * ignores non alphanumeric characters
    * reverses both numbers and alphabetic characters
    
    Examples:
    reversal("computers")) -> "sretupmoc"
    reversal("3294872309") -> ""
    '''
    return removal(s[::-1])

## Not palindrome
check.set_print_exact("sretupmoc")
check.expect("Q2T3:", print(reversal("computers")), None)  

## all numbers
check.set_print_exact("")
check.expect("Q2T4", print(reversal("3294872309")), None)

def alphabetic_palindrome(phrase):
    '''
    Returns either True or False to see if the phrase is an alphabetic 
    palindrome.
    
    alphabetic_palindrome: Str -> Bool
    
    requires:
    * ignores non alphanumeric characters and numbers and would return True
      because of the removal would make it an empty string
    
    Examples:
    alphabetic_palindrome("moM") -> True
    alphabetic_palindrome("computers") -> False
    alphabetic_palindrome("rAce .car 12") -> True
    alphabetic_palindrome("") -> True)
    '''
    if removal(phrase) == reversal(phrase):
        return True
    else:
        return False

## Ignores upper case       
check.expect("Q2E1:",alphabetic_palindrome("moM"), True)

## Not palindrome
check.expect("Q2E2:",alphabetic_palindrome("computers"), False)

## Ignores non-alphanum, space, numbers
check.expect("Q2E3:",alphabetic_palindrome("rAce .car 12"), True)

## Empty
check.expect("Q2E4:",alphabetic_palindrome(""), True)

## All numbers
check.expect("Q2T5:",alphabetic_palindrome("3294872309"), True)

## Palindrome numbers
check.expect("Q2T6:",alphabetic_palindrome("123321"), True)

## One space
check.expect("Q2T7",alphabetic_palindrome(" "), True)

## All non-alphanum
check.expect("Q2T8",alphabetic_palindrome("{<::"), True)

## Palindrome with num and nonalpha mix
check.expect("Q2T9",alphabetic_palindrome("Hel!L0o O11LL3eh"), True)

## Not a palindrome with num and nonalpha mix
check.expect("Q2T10",alphabetic_palindrome("Hel!L0o O1L3eh"), False)

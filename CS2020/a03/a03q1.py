##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 03, Question 1
##===============================================

## Question 1

import check

def compare_and_replace(s):
    '''
    Returns a string with characters in s that are the same as the third 
    character with "#"
    
    compare_and_replace: Str -> Str
    
    requires:
    * if the str length is < 3 then it returns the str
    
    Examples:
    compare_and_replace("bubble") -> "#u##le"
    compare_and_replace("me") -> "me"
    '''
    third_char = s[2:3]
    if len(s) < 3:
        return s   
    if s == "":
        return ""
    if s[0] == third_char:
        return s.replace(third_char,"#") 
    else:
        return s.replace(third_char,"#") 

## Replacing same char
check.expect("Q1T1:", compare_and_replace("bubble"), "#u##le") 

## Str < 3
check.expect("Q1T2:", compare_and_replace("me"), "me")

def keep_third_char(s):
    '''
    Returns a string that keeps the third character as is, but all other 
    characters that are the same as the third are replaced by "#"
    
    keep_third_char: Str -> Str
    
    Examples
    keep_third_char("bubble") -> "#ub#le"
    keep_third_char("me") ->"me"
    '''
    third_char = s[2:3]
    s = compare_and_replace(s)
    final_str = s[:2] + third_char + s[3:]
    return final_str

## All occurence of b replaced with "#" except third char
check.expect("Q1T4:",keep_third_char("bubble"),"#ub#le")

## String length <3
check.expect("Q1T5:", keep_third_char("me"),"me")

def new_word(s):
    '''
    Consume a string s and returns a string where all occurences of the third
    character of s have been replaced #, except for the third character itself.
    
    new_word: Str -> Str
    
    require:
    * if the string is less than 3 then the string will not be replaces with #
    
    Examples:
    
    new_word("me") -> "me"
    new_word("bubble") -> "#ub#le"
    new_word("") -> ""
    new_word("big") -> "big"
    '''
    return keep_third_char(s)

## Less than 3 char
check.expect("Q1E1:", new_word("me") , "me")

## More than 3 char
check.expect("Q1E2:", new_word("bubble"), "#ub#le")

## Empty case
check.expect("Q1E3:",new_word(""),"")

## All same char
check.expect("Q1T6:",new_word("ssss"),"##s#")

## Ignores upper, and space
check.expect("Q1T7:", keep_third_char("william biLLiam"),"wil#iam biLLiam")

## Ignores numbers,non-alphanum
check.expect("Q1T8:", keep_third_char("mell!12    smeLls"),"mel#!12    smeL#s")

## Number occurence
check.expect("Q1T9:",new_word("1214113415"),"#214##34#5")

## non-alpha occurence
check.expect("Q1T10",new_word("hi!! whassup!?!?!?!"),"hi!# whassup#?#?#?#")

## UPPERCASE
check.expect("Q1T11:",new_word("HELLO WORLLLD!"),"HEL#O WOR###D!")

## UPPERCASE and lowercase
check.expect("Q1T12:",new_word("HelLOwORllLd"),"HelLOwOR##Ld")

## Exactly 3 char
check.expect("Q1T13:",new_word("big"),"big")

## Space occurence
check.expect("Q1T14:",new_word("Hi HOW aRe y o U"),"Hi HOW#aRe#y#o#U")

## one space
check.expect("Q1T15:",new_word(" ")," ")

## a lot of space
check.expect("Q1T15:",new_word("          "),"## #######")
###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 04 Question 3
### ***************************************************
###
import check

def expand_strings(L,s,i):
  '''
  Consumes a list of string, L, a string s, and a natrual number i, and mutates 
  the list such that each element in L is expanded by creating a new string by 
  placing s at location i. 
  
  expand_strings: (listof Str) Str Nat -> None
  
  requires: 
  * if i is greater than the length of a string in L, s is appended to the end 
    of the string
  
  Examples:
  L1 = ["h"]
  L2 = ["cat", "dog", "hamster"]
  L5 = [""]
  L6 = []
  expand_strings(L1, "eight", 1) -> None
    and prints ["height"]
  expand_strings(L2, "12345", 4) -> None
    and prints ["cat12345", "dog12345", "hams12345ter"]
  expand_strings(L5, "111", 4) -> None
    and prints ["111"]
  expand_strings(L6, "111", 4) -> None
    and prints [""]
  '''
  L[:] = list(map(lambda old_string: old_string[0:i] + s + old_string[i:], L))
  print(L)

## Examples
L1 = ["h"]
L2 = ["cat", "dog", "hamster"]
L3 = ["helloworld", "alphabet", "university"]
L4 = ["hi", "me", "it"]
L5 = [""]
L6 = []
L7 = ["cat", "doggo", "hamster"]
L8 = ["a", "b", "c"]
## i is equal to the length of string in L
check.set_screen(["height"])
check.expect("Q3E1", expand_strings(L1, "eight", 1), None)
# list with strings less than the index and a string more than the index
check.set_screen(['cat12345', 'dog12345', 'hams12345ter'])
check.expect("Q3E2", expand_strings(L2, "12345", 4), None)

## Tests
## list with strings with lengths more than the index
check.set_screen(["hell111oworld", "alph111abet", "univ111ersity"])
check.expect("Q3T1", expand_strings(L3, "111", 4), None)

## list with strings of same length but is less than the index
check.set_screen(["hi111", "me111", "it111"])
check.expect("Q3T2", expand_strings(L4, "111", 4), None)

## list with an empty string
check.set_screen(["111"])
check.expect("Q3T3", expand_strings(L5, "111", 4), None)

## list with no strings
check.set_screen([])
check.expect("Q3T4", expand_strings(L6, "111", 4), None)

## list with str lenth < i, str length == i, str length > i
check.set_screen(['cat!!!', 'dogg!!!o', 'hams!!!ter'])
check.expect("Q3T5", expand_strings(L6, "!!!", 4), None)

## list all one length and index > str length
check.set_screen(['a!!!', 'b!!!', 'c!!!'])
check.expect("Q3T6", expand_strings(L7, "!!!", 4), None)

## list all one length and index < str length (index 0)
check.set_screen(['!!!a', '!!!b', '!!!c'])
check.expect("Q3T7", expand_strings(L8, "!!!", 0), None)

## using a negative index
check.set_screen(['hi11!!!1', 'me11!!!1', 'it11!!!1'])
check.expect("Q3T8", expand_strings(L4, "!!!", -1), None)

## using a negative index larger than length of str
check.set_screen(['!!!hi11!!!1', '!!!me11!!!1', '!!!it11!!!1'])
check.expect("Q3T9", expand_strings(L4, "!!!", -11), None)




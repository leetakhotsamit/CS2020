##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 03, Question 3
##===============================================
import check

## Question 3

def compare_and_replace(s1,s2):
  '''
  Returns a string by comparing two strings (s1, s2) of the same length to see 
  if the characters are the same at the same index position.If the characters
  are not the same then it is replaced with a dash
  
  compare_and_replace: Str Str -> Str
  
  requires: 
  * s1 and s2 are the same length
  
  Examples:
  compare_and_replace("steep","stoop") -> "st--p"
  compare_and_replace("meat","food") -> "----"
  
  '''
  if s1 == "":
    return ""
  if s1[0] == s2[0]:
    return s1[0] + compare_and_replace(s1[1:],s2[1:])
  else:
    return "-" + compare_and_replace(s1[1:],s2[1:])
  
## Contains same chars in strings of two different words
check.expect("Q3T1:",compare_and_replace("steep","stoop"),"st--p")

## No same characters
check.expect("Q3T2:",compare_and_replace("meat","food"),"----")

def update_dashes(secret, dashes, guess):
  '''
  Prints the updated version of dashes if the guess is in the secret. The 
  function consumes three strings:
  * secret, which is the word that the player is attempting to guess
  * dashes, which is the representation of secret using a string of hyphens,
    and any guessed letters if there are any
  * guess, is the players newest guess
  
  Effects: Prints to screen
  
  update_dashes: Str Str Str -> None
  
  requires:
  * dashes is the same length as secret
  * guess is exactly one character
  * secret, dashes and guess are non-empty strings and are all lower case
  
  Examples
  update_dashes("bubble", "------", "b") -> None 
  and prints "b-bb--"
  
  update_dashes("bubble", "b-bb--", "e") -> None 
  and prints "b-bb-e"
  
  update_dashes("python", "p-----", "x") -> None 
  and prints "p-----"
  
  update_dashes("cs", "-s", "c") -> None 
  and prints "cs"
  '''
  replace_dashes= dashes.replace("-", guess)
  answer = compare_and_replace(secret,replace_dashes)  
  print(answer)

## Guess at end str
check.set_screen("b-bb-e")
check.expect("Q3E1:", update_dashes("bubble", "b-bb--", "e"), None)

## Replacing more than 1 of the same char in dashes
check.set_screen("b-bb--")
check.expect("Q3E2:", update_dashes("bubble", "------", "b"), None)

## Guess not in secret
check.set_screen("p-----")
check.expect("Q3E3:", update_dashes("python", "p-----", "x"), None)

## Types of dashes: Case 1
check.set_screen("c-")
check.expect("Q3E4:", update_dashes("cs", "--", "c"), None)

## Types of dashes: Case 2
check.set_screen("-s")
check.expect("Q3E5:", update_dashes("cs", "--", "s"), None)

## Finishing the secret phrase
check.set_screen("cs")
check.expect("Q3E6: types of dashes", update_dashes("cs", "c-", "s"), None)

## Guessing same letter
check.set_screen("b-bb--")
check.expect("Q3T3:", update_dashes("bubble", "b-bb--", "b"), None)

## Completing secret word
check.set_screen("bubble")
check.expect("Q3T4:", update_dashes("bubble", "bubb-e", "l"), None)

## Letter in secret sentence
check.set_screen("--ll- ---l-")
check.expect("Q3T5:", update_dashes("Hello World", "----- -----", "l"), None)

## Completing secret sentence
check.set_screen("Hello World")
check.expect("Q3T6:", update_dashes("Hello World", "Hell- W-rld", "o"), None)


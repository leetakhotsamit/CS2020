###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 05 Question 01
### ***************************************************
###
import check

def scores(letter):
  '''
  Scores consumes a letter found in a word and returns the score the letter 
  which is either 1,2,4 or 8 if the letter is found in the word.
  
  scores: Str -> Nat
  
  requires:
  * 1point: A,E,I,L,N,O,R,S,T,U 
  * 2points: B,C,D,G,M,P
  * 4points: F,H,K,V,W,Y
  * 8points: J,Q,X,Z
  
  examples 
  scores("U") -> 1
  scores("Z") -> 8
  '''
  if letter in ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"]:
    return 1
  
  if letter in ["B", "C", "D", "G", "M", "P"]:
    return 2
  
  if letter in ["F", "H", "K", "V", "W", "Y"]:
    return 4
  
  else:
    return 8

# Test
check.expect("Q1T1", scores("U"), 1)
check.expect("Q1T2", scores("Z"), 8)
  
def word_score(word, points): 
  '''
  Consumes a word and provides a score to each letter in the word. The function 
  then returns the sum the points for each letter in the word.
  
  word_score: Str Nat -> Nat
  
  requires: 
  * points base case is to start at 0 
  
  examples:
  word_score("Hello", 0) -> 8
  word_score("zyZZyx", 0) -> 40
  '''
  if word == "":
    return points
  
  else:
    points = scores(word[0]) + word_score(word[1:],points)
    print(points)
  return points

# Test
check.expect("Q1T3", word_score("HELLO", 0), 8)
check.expect("Q1T4", word_score("ZYZZYX", 0), 40)

def scrabble_score(s):
  '''
  Consumes a string (s), and returns a score. Every letter is assigned a 
  different point. 
  
  Effect: prints "Invalid Character!" if there is a non-alphanumeric character
          present in the word
          
  requires:
  * 1point assigned to A,E,I,L,N,O,R,S,T,U 
  * 2points assigned to B,C,D,G,M,P
  * 4points assigned to F,H,K,V,W,Y
  * 8points assigned J,Q,X,Z
  
  scrabble_score: Str -> Nat
  
  examples:
  scrabble score("Hello!") -> 0 
    and prints "Invalid character!"
  scrabble score("") -> 0 
    and prints "Invalid character!"
  scrabble score("Hello") -> 8
  '''
  if not s.isalpha():
    print("Invalid character!")
    return 0
  s = s.upper()
  return word_score(s,0)

# Examples
check.expect("Q1E1", scrabble_score("Hello"), 8)
check.set_print_exact("Invalid character!")
check.expect("Q1E2", scrabble_score("Hello!"), 0)
check.expect("Q1E3", scrabble_score("zyZZyx"), 40)
check.set_print_exact("Invalid character!")
check.expect("Q1E4", scrabble_score("I like zyZZyx"), 0)

# Test
# all lower case letters
check.expect("Q1T5", scrabble_score("helloworld"), 17)
# empty string
check.set_print_exact("Invalid character!")
check.expect("Q1T6", scrabble_score(""), 0)
# one space
check.set_print_exact("Invalid character!")
check.expect("Q1T7", scrabble_score(" "), 0)
# all upper characters
check.expect("Q1T8", scrabble_score("HELLOWORLD"), 17)
# entire alphabet lower
check.expect("Q1T9", scrabble_score("abcdefghijklmnopqrstuvwxyz"), 78)
# only letters assigned 1 point
check.expect("Q1T10", scrabble_score("aeilnorstu"), 10)
# only letters assigned 2 points
check.expect("Q1T11", scrabble_score("bcdgmp"), 12)
# only letters assigned 4 points
check.expect("Q1T12", scrabble_score("fhkvwy"), 24)
# only letters assigned 8 points
check.expect("Q1T13", scrabble_score("jqxz"), 32)
# more than 10 chars
check.expect("Q1T14", scrabble_score("jqxsdkjfhwkjfhSFRGz"), 87)

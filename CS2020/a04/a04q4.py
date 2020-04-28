###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 04 Question 4
### ***************************************************
###
import check

## Question 4.1: Match
def match_compare(L1,L2):
    '''
    Consumes and compares two lists, L1 and L2, and returns a string including 
    numbers that are found in both L1 and L2 at the same position in the list
    
    match_compare: (listof Int) (listof Int) -> Str
    
    Examples:
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 2]
    L3 = [1, 2, 3, 4, 4, 5, 5]
    match_compare(L1,L2) -> "2"
    match_compare(L1,L3) -> "1234"
    '''
    L1 = ("".join(map(str,L1)))
    L2 = ("".join(map(str,L2)))
    if L1 == "":
        return ""
    if L2 == "":
        return ""    
    if L1[0] == L2[0]:
        return L1[0] + match_compare(L1[1:],L2[1:])
    else:
        return "" + match_compare(L1[1:],L2[1:])

## Test
L1 = [1, 2, 3, 4, 5]
L2 = [4, 2]
L3 = [1, 2, 3, 4, 4, 5, 5]
L4 = []
check.expect("Q4T1", match_compare(L1,L2), "2")
check.expect("Q4T2", match_compare(L1,L3), "1234")

def match(L1,L2):
    '''
    Consumes two list of integers, L1 and L2, and returns the number of elements
    that occur in the same position in the lists
    
    match: (listof Int) (listof Int) -> Nat
    
    Examples:
    match(L1, L2) -> 1 
    match(L1, L3) -> 4
    '''
    return len(match_compare(L1,L2)) 

## Test
check.expect("Q4T3", match(L1,L2), 1)
check.expect("Q4T4", match(L1,L3), 4)

## Question 4.2: Intersection Size

def build_list(old, new):
    '''
    Returns a new list by comparing if a number from the old list at index 0 
    is in the new list, if not then the number is added to the new list
    
    build_list: (listof Int) (listof Int) -> (listof Int)
    
    Examples:
    build_list([1,2,3,4], [1,1,1]) -> [1, 1, 1, 2, 3, 4]
    build_list([1,2,3,4], []) -> [1, 2, 3, 4]
    '''
    if old == []:
        return new
    elif old[0] in new:
        return build_list(old[1:], new)
    else:
        return build_list(old[1:], new + [old[0]])

## Test
check.expect("Q4T5", build_list([1,2,3,4], []), [1,2,3,4])
    
def intersection_size(L1,L2):
    '''
    Consumes two lists, L1 and L2, and returns the number of common elements 
    between the lists
    
    intersection_size: (listof Int) (listof Int) -> Nat
    
    Requires: 
    * if L1 contains exactly one instance of a number and L2 contains multiple
      instances of the number and the same vice versa then there is 1 element 
      shared between the lists

    Examples:
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 2]
    L3 = [1, 2, 3, 4, 4, 5, 5] 
    intersection_size(L1, L2) -> 2 
    intersection_size(L1, L3) -> 5
    '''
    intersect = list(filter(lambda x: x in L1, L2))
    new_list = build_list(intersect, [])
    return len(new_list)

## Test
check.expect("Q4T5", intersection_size(L1, L2), 2)
check.expect("Q4T6", intersection_size(L1, L3), 5)

## Question 4.3: Programming Mastermind

def incorrect_place(str_to_int,secret, correct):
    '''
    Compares two list of integers, str_to_int and secret, and based on how many
    are correct between the two list, the function returns the number of
    incorrect
    
    incorrect_place: (listof Int) (listof Int) Nat -> Nat
    
    Examples:
    incorrect_place([1,2,1,4],[1,6,1,4], 3) -> 1
    incorrect_place([1,2,0,4],[1,6,1,0], 0) -> 2
    '''
    intersect = list(filter(lambda x: x in str_to_int, secret))
    if intersection_size(intersect,str_to_int) == correct:
        return 0
    return intersection_size(intersect,str_to_int) and match(intersect,str_to_int)

## Test
check.expect("Q4T7", incorrect_place([1,2,1,4],[1,6,1,4], 3), 1)
check.expect("Q4T8", incorrect_place([1,2,0,4],[1,6,1,0], 0), 2)

def intersection(L1,L2):
    '''
    Compares two list, L1 and L2, and returns a list of common integers among 
    the two lists
    
    intersection: (listof Int) (listof Int) -> (listof Int)
    
    Examples:
    intersection([6,5,1],[1,6,5]) -> [6, 5, 1]
    intersection([6,5,1],[1,1,1]) -> [1]
    '''
    intersect = list(filter(lambda x: x in L2, L1))
    new_list = build_list(intersect, [])
    return new_list

## Test
check.expect("Q4T9", intersection([6,5,1],[1,6,5]), [6,5,1])
check.expect("Q4T10", intersection([6,5,1],[1,1,1]), [1])

def mastermind_helper(secret,turns, n):
    '''
    Consumes a secret list of numbers (secret), the number of turns left (turns)
    and the maximum turns of the guesser (n). Returns the number of guesses the
    guesser has left if there are still turns left or returns None when turns
    run out. And the following is printed:
      * prints the numbers in the correct and incorrect places
      * prints number of guesses to find the sequence (guess has to be correct)  
      * prints game over and the numbers in the correct and incorrect 
    
    mastermind_helper: (listof Int) Nat Nat -> None
    
    requires: 
      * secret is at least two and max the guesser
      * If last attempt (turns = 1) is incorrect, then return None and print
        prints game over and the numbers in the correct and incorrect
      * If last attempt (turns = 0) is incorrect, then return None and print
        prints game over and the numbers in the correct and incorrect
      * Print numbers in the correct and incorrect places if there are still 
        turns > 1
        
    Examples:
    If the user inputs "1 2 3 4" after calling 
       mastermind_helper([1,6,1,4], 7 - 1, 7)) -> None
       and "There are 2 numbers in correct places and 0 numbers in incorrect 
       places." is printed.
    
    If the user inputs "1 2 3 4" after calling 
       mastermind_helper([1,6,1,4], 1 - 1, 7)) -> None
       and "There are 2 numbers in correct places and 0 numbers in incorrect 
       places." \n"Sequence of 1 6 1 4 not found. Game Over." is printed.
    
    
    '''
    countdown = "There are {0} numbers in correct places and {1} numbers in incorrect places."
    guess_correct = "Sequence found in {0} guesses."
    input_prompt = input("Enter your guess: ")
    input_to_list = input_prompt.split(" ")
    str_to_int = list(map(int,input_to_list))
    secret_str = list(map(str,secret))
    str_space = " ".join(secret_str)
    correct = match(str_to_int, secret)
    incorrect = incorrect_place(str_to_int, secret, correct)
    reverse_intersection = intersection(str_to_int[::-1],secret)
    intersect = intersection(str_to_int, secret)
    
    if correct == len(secret) and correct:
        print(guess_correct.format(n - turns))
        return n - turns
    
    if reverse_intersection == secret and n == 1:
        print(countdown.format(0, len(secret)))
        return None    
    
    if intersection(secret, intersect) == secret:
        print(countdown.format(correct, len(secret) - correct))
        return mastermind_helper(secret,turns - 1, n)        
    
    elif reverse_intersection == secret:
        print(countdown.format(0, len(secret)))
        return mastermind_helper(secret,turns - 1, n)     
    
    elif n == 1 and secret != str_to_int:
        print(countdown.format(correct, incorrect)) 
        print("Sequence of" + " " + str_space + " " + "not found. Game Over.")
        return None
    
    elif turns == 0 and secret != str_to_int:
        print(countdown.format(correct, incorrect)) 
        print("Sequence of" + " " + str_space + " " + "not found. Game Over.")
        return None 
    
    elif n == 0 and secret != str_to_int:
        print(countdown.format(correct, incorrect)) 
        print("Sequence of" + " " + str_space + " " + "not found. Game Over.")
        return None       
    
    else:
        print(countdown.format(correct, incorrect)) 
        return mastermind_helper(secret,turns - 1, n)   

## Test
check.set_input("1 2 3 4")
check.set_print_exact("There are 2 numbers in correct places and 0 numbers in incorrect places.",
                      "Sequence of 1 6 1 4 not found. Game Over.")
check.expect("Q4T11", mastermind_helper([1,6,1,4], 1 - 1, 7), None)
check.set_input("1 6 1 4")

check.set_print_exact("Sequence found in 1 guesses.")
check.expect("Q4T12", mastermind_helper([1,6,1,4], 7 - 1, 7), 1)
    
def mastermind(secret, turns):
    '''
     Consumes a secret list of numbers (secret), the number of turns 
     left (turns). Returns the number of guesses the guesser has left if there
     are still turns left or returns None when turns run out. And the 
     following is printed:
      * prints the numbers in the correct and incorrect places
      * prints number of guesses to find the sequence (guess has to be correct)  
      * prints game over and the numbers in the correct and incorrect 
    
    mastermind: (listof Int) Nat -> None 
    
    requires: 
      * secret is at least two and max the guesser
      * If last attempt (turns = 1) is incorrect, then return None and print
        prints game over and the numbers in the correct and incorrect
      * If last attempt (turns = 0) is incorrect, then return None and print
        prints game over and the numbers in the correct and incorrect
      * Print numbers in the correct and incorrect places if there are still 
        turns > 1
    
    Examples
    If the user inputs "1 2 3 4" after calling 
       mastermind_helper([1,6,1,4], 7)) -> None
       and "There are 2 numbers in correct places and 0 numbers in incorrect 
       places." is printed.
    
    If the user inputs "1 6" after calling 
       mastermind_helper([1,6], 1)) -> None
       and "Sequence found in 1 guesses." is printed.
    '''
    return mastermind_helper(secret, turns - 1, turns)

## Examples:
## Sequence found in 4 guesses
check.set_input("1 2 3 4", "6 2 3 5", "1 1 6 4", "1 6 1 4")
check.set_print_exact("There are 2 numbers in correct places and 0 numbers in incorrect places.",
                      "There are 0 numbers in correct places and 1 numbers in incorrect places.",
                      "There are 2 numbers in correct places and 2 numbers in incorrect places.",
                      "Sequence found in 4 guesses.")
check.expect("Q4E1", mastermind([1,6,1,4], 5), 4)

## Last attempt: Sequence not found and turn is 1
check.set_input("1 2")
check.set_print_exact("There are 1 numbers in correct places and 0 numbers in incorrect places.",
                      "Sequence of 1 6 not found. Game Over.")
check.expect("Q4E2", mastermind([1,6], 1), None)

## Tests
## Turns is zero and guess is incorrect
check.set_input("1 2")
check.set_print_exact("There are 1 numbers in correct places and 0 numbers in incorrect places.",
                      "Sequence of 1 6 not found. Game Over.")
check.expect("Q4T13", mastermind([1,6], 0), None)

## Turn is 1, last attempt is correct
check.set_input("1 6")
check.set_print_exact("Sequence found in 1 guesses.")
check.expect("Q4T14", mastermind([1,6], 1), 1)

## Last attempt is correct
check.set_input("1 6")
check.set_print_exact("Sequence found in 1 guesses.")
check.expect("Q4T15", mastermind([1,6], 1), 1)

## Guess 1: is in reverse, Last attempt: correct
check.set_input("6 1", "1 6")
check.set_print_exact("There are 0 numbers in correct places and 2 numbers in incorrect places.",
                      "Sequence found in 2 guesses.")
check.expect("Q4T16", mastermind([1,6], 3), 2)

## Using the same numbers in different string combinations
check.set_input("6 5 1", "5 6 1", "6 1 5", "1 6 5")
check.set_print_exact("There are 0 numbers in correct places and 3 numbers in incorrect places.",
                      "There are 1 numbers in correct places and 2 numbers in incorrect places.",
                      "There are 1 numbers in correct places and 2 numbers in incorrect places.",
                      "Sequence found in 4 guesses.")
check.expect("Q4T17", mastermind([1,6,5], 4), 4)

## secret is empty string
check.set_input("6 5 1", "5 6 1", "6 1 5", "1 6 5")
check.set_print_exact("There are 0 numbers in correct places and 0 numbers in incorrect places.",
                      "There are 0 numbers in correct places and 0 numbers in incorrect places.",
                      "There are 0 numbers in correct places and 0 numbers in incorrect places.",
                      "There are 0 numbers in correct places and 0 numbers in incorrect places.",
                      "Sequence of  not found. Game Over.")
check.expect("Q4T18", mastermind([""], 4), None)

##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 02, Question 3
##===============================================

## Question 4
import math
import check

def final_jeopardy(c1, c2, c3):
  '''
  Consumes three natural numbers and returns the minimum amount that the leader
  should bet in order to gurantee victory if they get the question correct. The 
  leader can be any of contestants (c1,c2,c3). To determine the leader the 
  maximum of the contestants needs to be known.
  
  final_jeopardy(c1, c2, c3): Nat Nat Nat -> Nat
  
  requires:
  * tie between second and leader, then both bet everything
  * leader is far ahead, bet is 0
  * max bet for second in place is double their amount, if the max amount is 
    equal to the leader then the leader bets 1 to win
  
  examples:
  final_jeopardy(5000, 7500, 10000) -> 5001 
  final_jeopardy(15000, 15000, 800) -> 15000
  '''
  m12 = max(c1,c2)
  m13 = max(c1, c3)
  m23= max(c2,c3)
  leader = max(c1,c2,c3)
  second = min(m12,m13,m23)  
  leader_max = leader * 2
  second_max = second * 2
  if leader == second:
    return leader
  if second_max == leader:
    return 1
  if second == 0:
    return 0
  if second < leader:
    return leader_max + 1 - second_max

## Test1: leader = second
check.expect("Q3T1",final_jeopardy(500, 500, 10),500)
check.expect("Q3T2",final_jeopardy(10, 200, 200), 200)
check.expect("Q3T3",final_jeopardy(200, 10, 200), 200)
## Test2: leader > second
check.expect("Q3T4",final_jeopardy(5000, 7500, 10000), 5001)
check.expect("Q3T5",final_jeopardy(10000, 7500, 5000), 5001)
check.expect("Q3T6",final_jeopardy(7500,5000,10000), 5001)
check.expect("Q3T7",final_jeopardy(7500,0,10000), 5001)
## Test3: second = 0
check.expect("Q3T8",final_jeopardy(0,0,10000), 0) 
check.expect("Q3T9",final_jeopardy(0,10000,0), 0) 
## Test4: second max bet = leader
check.expect("Q3T10",final_jeopardy(5000, 0, 10000), 1)
check.expect("Q3T11",final_jeopardy(0, 10000,5000), 1)




##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 02, Question 1
##===============================================

## Question 1
import math
import check

def cs116_grade(assign, mid, fin, part):
  '''
  Returns the grade based on the grading scheme, 20% Assts, 30% mid_exam, 45% final_exam 5% for clickers and tutorials times.
  
  earned_grade: Float Float Float Float => Int
  
   Require:
   * assign, mid, fin, part are floating point value 
     between 0 and 100 (inclusive)
   
   Examples:
   cs116_grade(75,60,80,90) => 74
   cs116_grade (80 ,52 ,40 ,100) => 45
   cs116_grade(0,55,60,0) => 44
  '''
  assign_weight = 0.2
  mid_weight = 0.3
  fin_weight = 0.45
  part_weight = 0.05
  exam_avg = (assign * assign_weight + fin * fin_weight)/ 75
  grade = (assign * assign_weight) + (mid * mid_weight) + (fin * fin_weight) + (part * part_weight)
  if exam_avg >= 0.5:
    return round(grade)
  else:
   return (round(min(45, grade)))

## Examples:
check.expect("Q1E1", cs116_grade(75,60,80,90), 74)
check.expect("Q1E2", cs116_grade (80 ,52 ,40 ,100), 45)
check.expect("Q1E3", cs116_grade(0,55,60,0), 44)

## Test1: exam average less than 50%, and grade is higher than 45
check.expect("Q1T1", cs116_grade(60.0,55.8,40.0,55.5), 45)
## Test2: exam average less than 50%, the grade is less than 45
check.expect("Q1T2", cs116_grade(10.0, 5.0, 40.0, 12.0), 22)
## Test3: exam average higher than 50%, the grade is less than 45
check.expect("Q1T3", cs116_grade(0, 51, 51, 0), 38)
## Test4: exam average higher than 50%, the grade is higher than 45
check.expect("Q1T4", cs116_grade(100, 100, 100, 100), 100)
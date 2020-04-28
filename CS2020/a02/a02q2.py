##===============================================
##   Leeta Khotsamit (20626249)
##   CS 116 Winter 2020
##   Assignment 02, Question 2
##===============================================

## Question 2

import math
import check

def after_tax(cost, prov_abbr, item):
   '''
   Returns the selling price of the item based on the cost and the appropriate
   tax applied based on the province. 
   
   after_tax: Float Str Str => Float
   
   requires:
   * food is expemt from all taxes
   * literature and child goods are expemted from PST but not GST 
   * SK tax (GST + PST) = 1.11
   * BC tax (GST + PST) = 1.12
   * MN and ON tax (GST + PST) = 1.13
   * QC tax (GST + PST) = 14.975
   * NB, NL, NS, PE tax (GST + PST) = 1.10
   '''
   GST = 0.05
   SK = 0.06
   BC = 0.07
   MB_ON = 0.08
   QC = 0.09975
   NB_NL_NS_PE = 0.10
   if item == "food":
     return cost
   if item == "literature" or item == "child":
     return cost * (1 + GST)
   if prov_abbr == "SK":
      return (cost * (1 + GST + SK))
   if prov_abbr == "BC":
      return cost * (1 + GST + BC)  
   if prov_abbr == "MB" or prov_abbr == "ON":
      return cost * (1 + GST + MB_ON) 
   if (prov_abbr == "NB" or prov_abbr == "NL" or 
       prov_abbr == "NS" or prov_abbr == "PE"):
      return cost * (1 + GST + NB_NL_NS_PE) 
   else:
      return cost * (1 + GST)

## Test1: Literature related goods
check.within("Q2T1", after_tax(20.0, "ON", "literature"), 21.0, 0.01)
## Test2: Child related goods
check.within("Q2T2", after_tax(25.0, "AB", "child"), 26.25, 0.01)
## Test3: Food related
check.within("Q2T3", after_tax(12.25, "NS", "food"), 12.25, 0.01)
## Test4: Goods in SK
check.within("Q2T4", after_tax(50100, "SK", "car"), 55611.00, 0.01)
## Test5: Goods in BC
check.within("Q2T5", after_tax(1000000, "BC", "house"), 1120000.00, 0.01)
## Test6: Goods in MB or ON
check.within("Q2T6", after_tax(1379, "ON", "gucci"), 1158.27, 0.01)
check.within("Q2T7", after_tax(9.99, "MB", "gym membership"), 11.28, 0.01)
## Test7: Goods in NB, NL, NS, PE
check.within("Q2T8", after_tax(14.99, "NB", "movies"), 17.24, 0.01)
check.within("Q2T9", after_tax(1.99, "NL", "toothpaste"), 2.29, 0.01)
check.within("Q2T10", after_tax(999, "NS", "iphone"), 1148.85, 0.01)
check.within("Q2T11", after_tax(20.99, "PE", "fishing rod"), 24.14, 0.01)
## Test8: Goods in AB, NT NU, YT
check.within("Q2T12", after_tax(46, "AB", "oil"), 48.3, 0.01)
check.within("Q2T13", after_tax(2500, "NT", "diamonds"), 2625, 0.01)
check.within("Q2T14", after_tax(120, "NU", "igloo ring"), 126, 0.01)
check.within("Q2T15", after_tax(5, "YT", "rock"), 5.25, 0.01)
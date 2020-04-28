## Question 3

def final_jeopardy(c1, c2, c3):
  c1_max = c1 * 2
  c2_max = c2 * 2
  c3_max = c3 * 2
  c1_max = c1 * 2
  c2_max = c2 * 2
  c3_max = c3 * 2
  m12 = max(c1,c2)
  m13 = max(c1, c3)
  m23= max(c2,c3)
  leader = max(c1,c2,c3)
  second = min(m12,m13,m23)  
  if c1 == c2:
    return c1
  
  elif c2 == c3:
    return c3
  
  elif c1 < c2:
    if c2 == c3:
      return c3    
    if c2 < c3:
      return c3_max + 1 - c2_max
    else:
      return c2_max + 1 - c1_max
    
  elif c1 == c2:
    if c2 == c3:
      return c3
    
  elif c1 > c2:
    if c2 == c3:
      return c3
    if c2 < c3:
      return c3_max + 1 - c2_max
    if c2 > c3:
        return c1_max + 1 - c2_max
      


print(final_jeopardy(500, 500, 10))
print(final_jeopardy(10, 200, 200))
print(final_jeopardy(5000, 7500, 10000))
print(final_jeopardy(5000, 7500, 7500))
print(final_jeopardy(200, 200, 200))
print(final_jeopardy(5000, 7500, 0))
print(final_jeopardy(10000, 7500, 5000))
print(final_jeopardy(7500, 10000, 5000))
print(final_jeopardy(0, 7500, 10000))
## help
print(final_jeopardy(5000, 0, 10000))


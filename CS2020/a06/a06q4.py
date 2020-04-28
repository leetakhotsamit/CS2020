###
### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 06 Question 4
### ***************************************************
###
###

import check

def frame(h,l,c):
  '''
  Consumes natural numbers for height and length, which are variable h and l 
  repectively, and a string character (c).
  
  effects: prints snake picture onto the screen 
  
  frame: Nat Nat Str -> None
  
  examples:
  frame(1,0,'#') -> None
    and prints
    #########
    #   --:~# 
    #  /    # 
    #--     # 
    #########
  '''
  line_size = 8 + h + 2*l*(h+2)
  snake_head = '--:~'
  num_lines = 4 + h
  #first_line
  print(line_size*c) 
  # second
  print(c + ' '*(2+h) + '--' + (' '*(2*h + 2) + '--')*l + ':~' + c)
  # height lines
  for i in range(h):
    s1 = c+ ' '*(1 + h - i) + '/'
    s2 = (' '*(2 + 2*i) + '\\' + ' '*(2*(h - i)) + '/')*l
    s3 = ' '*(4+i) + c
    print(s1+s2+s3)
  # second last
  print(c + '--' + (' '*(2*h + 2) + '--')*l + ' '*(4+h)+c)
  # last line
  print(line_size*c)

# Test
check.set_print_exact('#########\n#   --:~#\n#  /    #\n#--     #\n#########')
check.expect('Q4T1',frame(1,0,'#'),None)

def snake(): 
  '''
  Reads an input from the user with inputs for height(Int), length(Int) 
  of the snake frame and the input of the framing character (Str).
  
  Effects:
  * reads input which is an integer for height or length
  * reads input which is a string for the framing character
  * prints to the screen
  
  snake(): None -> None
  
  requires:
  * height cannot be 0
  * each line has a minimum size length of 8 + height + 2*length*(height+2)
  * first and last lines are framing characters
  
  examples
  Enter height: 1
  Enter length: 0
  Enter frame: #
  #########
  #   --:~# 
  #  /    #
  #--     # 
  #########
  
  Enter height: a 
    and prints Invalid input.
  Enter height: 0 
    and prints Invalid input.
  Enter height: 3
  Enter length: 1
  Enter frame: $$ 
    and prints Invalid input.
  Enter frame: hello 
    and prints Invalid input.
  Enter frame: 
  * ********************* 
  *      --          --:~*
  *    /    \      /     *
  *   /      \    /      *
  *  /        \  /       *
  *--          --        *
  * *********************
  '''
  height = input("Enter height: ")
  while (height.isdigit() == False) or (int(height) == 0):
    print('Invalid input.')
    height = input("Enter height: ")  
  length = input("Enter length: ")
  while (length.isdigit() == False):
    print('Invalid input.')
    length = input("Enter length: ")    
  f = input("Enter frame: ")     
  while (len(f) != 1):
    print('Invalid input.')
    f = input("Enter frame: ")  
  if height.isdigit() and length.isdigit() and (len(f) == 1):    
    frame(int(height),int(length),f)
  else:
    print('Invalid input.')
    snake()
    
# Examples
check.set_input('1','0','#')
check.set_print_exact('#########\n'+
                      '#   --:~#\n'+
                      '#  /    #\n'+
                      '#--     #\n'+
                      '#########')
check.expect('Q4T2', snake(),None)

check.set_input('a','0','3','1','$$','hello','*')
check.set_print_exact('Invalid input.',
                      'Invalid input.',
                      'Invalid input.',
                      'Invalid input.',
                      '*********************\n' +
                      '*     --        --:~*\n' +
                      '*    /  \      /    *\n' +
                      '*   /    \    /     *\n'
                      '*  /      \  /      *\n'+
                      '*--        --       *\n' +
                      '*********************')
check.expect('Q4T3', snake(),None)

# Test
# frame is a number
check.set_input('0','0','1','2','6')
check.set_print_exact('Invalid input.',
                      'Invalid input.',
                      '666666666666666666666\n'+
                      '6   --    --    --:~6\n'+
                      '6  /  \  /  \  /    6\n'+
                      '6--    --    --     6\n'+
                      '666666666666666666666')
check.expect('Q4T4', snake(),None)
# height 1, length1
check.set_input('1','1','!')
check.set_print_exact('!!!!!!!!!!!!!!!\n'+
                      '!   --    --:~!\n'+
                      '!  /  \  /    !\n'+
                      '!--    --     !\n'+
                      '!!!!!!!!!!!!!!!')                    
check.expect('Q4T5', snake(),None)
#height 4, length 4, frame a character
check.set_input('4','4','T')
check.set_print_exact('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\n'+
                      'T      --          --          --          --          --:~T\n'+
                      'T     /  \        /  \        /  \        /  \        /    T\n'+
                      'T    /    \      /    \      /    \      /    \      /     T\n'+
                      'T   /      \    /      \    /      \    /      \    /      T\n'+
                      'T  /        \  /        \  /        \  /        \  /       T\n'+
                      'T--          --          --          --          --        T\n'+
                      'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')                    
check.expect('Q4T6', snake(),None)
# height 1, length 4
check.set_input('1','4','i')
check.set_print_exact('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n'+
                      'i   --    --    --    --    --:~i\n'+
                      'i  /  \  /  \  /  \  /  \  /    i\n'+
                      'i--    --    --    --    --     i\n'+
                      'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')    
check.expect('Q4T7', snake(),None)
# height 4, length 1
check.set_input('4','1','$')
check.set_print_exact('$$$$$$$$$$$$$$$$$$$$$$$$\n'+
                      '$      --          --:~$\n'+
                      '$     /  \        /    $\n'+
                      '$    /    \      /     $\n'+
                      '$   /      \    /      $\n'+
                      '$  /        \  /       $\n'+
                      '$--          --        $\n'+
                      '$$$$$$$$$$$$$$$$$$$$$$$$')    
check.expect('Q4T8', snake(),None) 
# height 4, length 0
check.set_input('4','0','$')
check.set_print_exact('rrrrrrrrrrrr\n'+
                      'r      --:~r\n'+
                      'r     /    r\n'+
                      'r    /     r\n'+
                      'r   /      r\n'+
                      'r  /       r\n'+
                      'r--        r\n'+
                      'rrrrrrrrrrrr')    
check.expect('Q4T79', snake(),None) 
# height correct, length invalid then correct
check.set_input('4','!','1','$')
check.set_print_exact('Invalid input.',
                      '$$$$$$$$$$$$$$$$$$$$$$$$\n'+
                      '$      --          --:~$\n'+
                      '$     /  \        /    $\n'+
                      '$    /    \      /     $\n'+
                      '$   /      \    /      $\n'+
                      '$  /        \  /       $\n'+
                      '$--          --        $\n'+
                      '$$$$$$$$$$$$$$$$$$$$$$$$')    
check.expect('Q4T10', snake(),None) 
# height invalid then correct, length correct
check.set_input('!','4','1','$')
check.set_print_exact('Invalid input.',
                      '$$$$$$$$$$$$$$$$$$$$$$$$\n'+
                      '$      --          --:~$\n'+
                      '$     /  \        /    $\n'+
                      '$    /    \      /     $\n'+
                      '$   /      \    /      $\n'+
                      '$  /        \  /       $\n'+
                      '$--          --        $\n'+
                      '$$$$$$$$$$$$$$$$$$$$$$$$')    
check.expect('Q4T11', snake(),None) 

snake()
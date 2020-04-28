### ***************************************************
###	Leeta Khotsamit (20626249)
###	CS 116 Winter 2020
###	Assignment 05 Question 04
### ***************************************************
###
import check

def less_than_100(n):
    """
    Consumes a natural number n and returns thr english spelling n as a string
    for n <= 99, produces None if number is over 99
    
    less_than_100: Nat -> Str
    
    requires: 
    * Nat number including zero 
    * numbers are <= 99
    
    examples:
    less_than_100(0) -> 'zero'
    less_than_100(80) -> 'eighty'
    """
    teens = ['zero', 'one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                    'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ['', 'ten','twenty', 'thirty', 'forty', 'fifty',
                   'sixty', 'seventy', 'eighty', 'ninety']
    if 0 <= n <= 19:
        # unique
        return teens[n]
    elif 20 <= n <= 99:
        # tens
        if n % 10 == 0:
            return tens[n // 10]
        return tens[n // 10] + ' ' + teens[n % 10]

# Test  
check.expect("Q4T1", less_than_100(80), 'eighty')
check.expect("Q4T2", less_than_100(0), 'zero')

def less_than_1000(n):
    """
     Consumes a natural number n and returns thr english spelling n as a string
    for n <= 999, produces None if number is over 999
    
    less_than_1000: Nat -> Str
    
    requires: 
    * Nat number including zero 
    * numbers are <= 999
    
    examples:
    less_than_1000(999) -> 'nine hundred ninety nine'
    less_than_100(80) -> 'eighty'
    """
    teens = ['zero', 'one', 'two', 'three', 'four', 'five',
                        'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                        'twelve', 'thirteen', 'fourteen', 'fifteen',
                        'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    tens = ['', 'ten','twenty', 'thirty', 'forty', 'fifty',
                       'sixty', 'seventy', 'eighty', 'ninety']
    answer = ''
    # hundreds
    answer += teens[n // 100] + ' hundred'
    # tens
    if n % 100 > 0:
        answer += ' ' + less_than_100(n % 100)
    return answer

# Test
check.expect("Q4T3", less_than_1000(999), 'nine hundred ninety nine')

def thousands(n):
    """
    Consumes a natural number n and returns thr english spelling n as a string
    for n <= 999999, produces None if number is over 999999
    
    thousands: Nat -> Str
    
    requires: 
    * Nat number including zero 
    * numbers are <= 999999
    
    examples:
    thousands(42713) -> 'forty two thousand seven hundred thirteen'
    """
    answer = ''
    if 0 <= n // 1000 <= 99:
        answer += less_than_100(n // 1000) + ' thousand'
    # hundreds of thousands
    else:
        answer += less_than_1000(n // 1000) + ' thousand'
    if 0 < n % 1000 <= 99:
        answer += ' ' + less_than_100(n % 1000)
    elif 100 <= n % 1000 <= 999:
        answer += ' ' + less_than_1000(n % 1000)
    return answer

# Test
check.expect("Q4T4", thousands(42713),\
             'forty two thousand seven hundred thirteen')

def millions(n):
    """
    Consumes a natural number n and returns thr english spelling n as a string
    for n <= 999999999, produces None if number is over 999999999
    
    millions: Nat -> Str
    
    requires: 
    * Nat number including zero 
    * numbers are <= 999999999
    
    examples:
    millions(4000000) -> 'four million'
    """
    answer = ''
    if 0 < n // 1000000 <= 99:
        answer += less_than_100(n // 1000000) + ' million'
    else:
        answer += less_than_1000(n // 1000000) + ' million'
    if 0 < n % 1000000 <= 99:
        answer += ' ' + less_than_100(n % 1000000)
    elif 100 <= n % 1000000 <= 999:
        answer +=  ' ' + less_than_1000(n % 1000000)
    elif 1000 <= n % 1000000 <= 999999:
        answer += ' ' + thousands(n % 1000000)
    return answer

# Test
check.expect("Q4T5", millions(4000000), 'four million')

def billions(n):
    """
    Consumes a natural number n and returns thr english spelling n as a string
    for n <= 999999999, produces None if number is over 999999999
    
    billions: Nat -> Str
    
    requires: 
    * Nat number including zero 
    * numbers are <= 999999999
    
    examples:
    billions(2000124001) -> 'two billion one hundred twenty four thousand one'
    """
    answer = ''
    if 0 < n // 1000000000 <= 99:
        answer += less_than_100(n // 1000000000) + ' billion'
    else:
        answer += less_than_1000(n // 1000000000) + ' billion'
    if 0 < n % 1000000000 <= 99:
        answer += less_than_100(n % 1000000000)
    elif 100 <= n % 1000000000 <= 999:
        answer +=  ' ' + less_than_1000(n % 1000000000)
    elif 1000 <= n % 1000000000 <= 999999:
        answer += ' ' + thousands(n % 1000000000)    
    elif 1000 <= n % 1000000000 <= 999999999:
        answer += ' ' + millions(n % 1000000000)
    return answer

# Test
check.expect("Q4T6", billions(2000124001), \
             'two billion one hundred twenty four thousand one')

def spell_number(n, group_names):
    """
    Consumes a natural number (n) and a list of strings (group_names) and returns
    the english spelling of n as a string
    
    requires:
    * n is a Nat number or zero
    * list group_names is at least as long as the number of digits in the number
      divided by three
    
    spell_number: Nat (listof Str) -> Str
    
    examples
    spell_number(0, [""]) -> "zero"
    spell_number(5555, ["flibberty", "floppity"]) -> 
       "five flibberty five hundred fifty five floppity"
    spell_number(123456789, ["billion", "million", "thousand", ""]) ->
       "one hundred twenty three million four hundred fifty six thousand seven
        hundred eighty nine"
    """
    s=str(n)
    strip_zeros = s.strip('0')
    length = n//3
    
    if 0 <= n <= 99:
        if strip_zeros == '' or len(strip_zeros) == 1 or '' in group_names:
            return less_than_100(n)
        if length >= len(group_names):
            return less_than_100(n) + ' ' + group_names[0]
        return less_than_100(n) 
    elif 100 <= n <= 999:   
        if len(strip_zeros) == 1:
            l = len(group_names) - 2
            return less_than_1000(n)
        if length >= len(group_names):
            return less_than_1000(n) + ' ' + group_names[0]
        return less_than_1000(n)
    elif 1000 <= n <= 999999:
        if len(strip_zeros) == 1:
            return thousands(n)        
        if length >= len(group_names):
            t = thousands(n)
            l = len(group_names) - 1
            return t.replace('thousand',group_names[0]) + ' ' + group_names[l]
        return thousands(n)
    elif 10000 <= n <= 999999999:  
        if len(strip_zeros) == 1:
            return millions(n) 
        if 'million' and 'thousand' in group_names:
            return millions(n) + ' ' + group_names[-1]
        if int(strip_zeros) >= len(group_names):
            t = millions(n)
            l = len(group_names) - 2
            s = t.replace('thousand',group_names[l]) 
            m = s.replace('million',group_names[0])
            return m 
        return millions(n)
    elif 100000 <= 999999: 
        if len(strip_zeros) == 1:
            return billions(n)
        if 'million' and 'thousand' and 'billion' in group_names:
            return billions(n) + ' ' +  group_names[-1]       
        if length >= len(group_names):
            t = billions(n)
            l = len(group_names) - 1
            l1 = len(group_names) - 2
            s = t.replace('thousand',group_names[l]) 
            m = s.replace('million',group_names[l1])
            b = m.replace('billion',group_names[0])
            return b 
        return billions(n)
    
# Examples
check.expect("Q4E1", spell_number(0, [""]), 'zero')
check.expect("Q4E2", spell_number(42, [""]), 'forty two')
check.expect("Q4E3", spell_number(900, ["units"]), 'nine hundred')
check.expect("Q4E4", spell_number(42713, ["thousand", ""]), \
             'forty two thousand seven hundred thirteen ')
check.expect("Q4E5", spell_number(4000000, ["million", "thousand", "units"]), \
             'four million')
check.expect("Q4E6", spell_number(8000010, ["million", "thousand", ""]), \
             'eight million ten ')
check.expect("Q4E7", spell_number(8000110, ["million", "thousand", ""]), \
             'eight million one hundred ten ')
check.expect("Q4E8", spell_number(81110,  ["thousand", ""]), \
             'eighty one thousand one hundred ten ')
check.expect("Q4E9", spell_number(5555, ["flibberty", "floppity"]),\
             'five flibberty five hundred fifty five floppity')
check.expect("Q4E10", \
             spell_number(2000124001,["billion","million","thousand","units"]), \
             'two billion one hundred twenty four thousand one units')

# Test
check.expect("Q4E11", \
             spell_number(199000,["units", '']), \
             'one hundred ninety nine units ')
check.expect("Q4E12", \
             spell_number(0,["apples"]), \
             'zero')
check.expect("Q4E12", \
             spell_number(999999,["apples", "bananas", "pears"]), \
             'nine hundred ninety nine apples nine hundred ninety nine pears')
check.expect("Q4E13", \
             spell_number(1,["apples", "bananas", "pears"]), \
             'one')
check.expect("Q4E14", \
             spell_number(10,["apples", "bananas", "pears"]), \
             'ten')
check.expect("Q4E15", \
             spell_number(100,["apples", "bananas", "pears"]), \
             'one hundred')
check.expect("Q4E16", \
             spell_number(1000,["apples", "bananas", "pears"]), \
             'one thousand')
check.expect("Q4E17", \
             spell_number(1000,["apples", "bananas", "pears"]), \
             'one thousand')
check.expect("Q4E18", \
             spell_number(10000,["apples", "bananas", "pears"]), \
             'ten thousand')
check.expect("Q4E19", \
             spell_number(1000000,["apples", "bananas", "pears"]), \
             'one million')
check.expect("Q4E20", \
             spell_number(1000000000,["apples", "bananas", "pears"]), \
             'one billion')
check.expect("Q4E21", \
             spell_number(111111,["apples", "bananas", "pears"]), \
             'one hundred eleven apples one hundred eleven pears')
check.expect("Q4E22", \
             spell_number(1111111111,["apples", "bananas", "pears"]), \
             'one apples one hundred eleven bananas one hundred eleven pears one hundred eleven')
check.expect("Q4E23", \
             spell_number(89,["apples", "bananas", "pears"]), \
             'eighty nine apples')
check.expect("Q4E24", \
             spell_number(891,["apples", "bananas", "pears",'orange']), \
             'eight hundred ninety one apples')

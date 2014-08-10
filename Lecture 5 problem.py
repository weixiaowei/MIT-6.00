#L5 problem 1
def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


#L5 problem 2
def recurPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """

    # exp could be 1, then return base.
    # But to figure out what base case to use,
    # think about what the smallest value of exp can be
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)


#L5 problem 3
def recurPowerNew(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base*recurPowerNew(base, exp-1)
    

#L5 problem 4
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    c = min(a, b)
    while a%c != 0 or b%c != 0:
        c -= 1
    return c


#L5 problem 5
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)



#Towers of Hanoi
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)



#Recursion on strings
def isPanlindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz'
            ans = ans + c
        return ans
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))



#L5 problem 6
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    num = 0
    for c in aStr:
        num += 1
    return num
    
    

#L5 problem 7
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr=='':
       return 0
    else:
       return 1+lenRecur(aStr[1:])



#L5 problem 8
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])



#L5 problem 9
#wrapper function calls
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1 and len(str2) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    else:
        return str1[0] == str2[-1] and return semordnilap(str1[1:], str2[:-1])



# Globe variables
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')


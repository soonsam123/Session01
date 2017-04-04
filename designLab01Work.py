# Name: Soon Sam R Santos
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1
import math

#-----------------------------------------------------------------------------

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1) + fib(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21.
print fib(1)   # 1
print fib(2)   # 1
print fib(8)   # 21

# Every time I call the function it will need to calculate once again.
# A better way to do this is to store the result in a dcitionary.
def fibonnaci(n):
    # Key: position; Value: Fibonnaci answers
    fib_numbers = {0: 0, 1: 1, 2: 1}
    if fib_numbers.has_key(n):
        return fib_numbers[n]
    else: 
        new_value = fibonnaci(n - 1) + fibonnaci(n - 2)
        fib_numbers[n] = new_value
        return new_value
print fibonnaci(1)   # 1
print fibonnaci(2)   # 1
print fibonnaci(8)   # 21 
print fibonnaci(20)  # 6765
# My dictionary have all the values from 0 to 20 now. I don't need to calculate them anymore.
print "--------------------------------------------" # Separating Exercises
#-----------------------------------------------------------------------------
# Create a new vectore of two real numbers.
# Convert a vector to a string __str__ module.
# Acess the components with getX() and getY() methods.
# Add two V2s to get a new V2 (with add and __add__ methods)
# Multiply V2 by a scalar and return a new V2 (with mul and __mul__ methods)
class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __add__(vector1, vector2):
        x = vector1.getX() + vector2.getX()
        y = vector1.getY() + vector2.getY()
        new_vector = V2(x, y)
        return new_vector
    def __mul__(vector1, num):
        x = vector1.getX() * num
        y = vector1.getY() * num
        new_vector = V2(x, y)
        return new_vector
vec1 = V2(3,4)
vec2 = V2(2,2)
print vec1.__add__(vec2)    # (5,6) So getX and getY is working.
print vec1 + vec2           # (5,6)__add__ override the + operator.
print vec1.__mul__(5)       # (15,20)
print vec1*5                # (15,20) __mul__ overrides the * operator.

print "--------------------------------------------" # Separating Exercises
#-----------------------------------------------------------------------------
# This is pretty straightforawrd, it doesn't look like so openly.
# But it is working!
class Polynomial:
    def __init__(self, list):
        self.coef = []
        j = 0
        for j in range(6 - len(list)):  # len(list) = 4 for j in range(2). from 0 to 2 (3 times)
            self.coef.append(float(0))
            j = j + 1
            
        i = 0
        while i < len(list):  # i from 0 to 3.
            self.coef.append(float(list[i]))
            i = i + 1
    def __str__(self):
        j = 5
        result = ''
        for i in range(len(self.coef)):    
            if self.coef[i] != 0:
                if j == 1:
                    result = result + str(self.coef[i])+" z "+" + "
                elif j == 0:
                    result = result + str(self.coef[i])
                else:
                    result = result + str(self.coef[i])+" z**"+str(j)+" + "
            j = j - 1
        return result
    def __add__(self, other):
        new_pol_coef = []
        for i in range(len(self.coef)):
            new_pol_coef.append(self.coef[i] + other.coef[i])
        new_pol = Polynomial(new_pol_coef)
        return new_pol

            
    def __call__(self,z):
        result = 0
        j = 5
        for i in range(len(self.coef)):
            result = result + (self.coef[i]*(z**j))
            j = j - 1
        return result

    def __mul__(self, other):
        # There may be pattern here to make the code smaller. Don't worry too much about it.
        # It will work at maximum for x**2 mul x**2.
        new_pol_coef = []
        new_pol_coef.append(self.coef[-3]*other.coef[-3])
        new_pol_coef.append(self.coef[-3]*other.coef[-2]+
                            self.coef[-2]*other.coef[-3])
        new_pol_coef.append(self.coef[-3]*other.coef[-1]+
                            self.coef[-2]*other.coef[-2]+
                            self.coef[-1]*other.coef[-3])
        new_pol_coef.append(self.coef[-2]*other.coef[-1]+
                            self.coef[-1]*other.coef[-2])
        new_pol_coef.append(self.coef[-1]*other.coef[-1])
        new_pol = Polynomial(new_pol_coef)
        return new_pol
    
    def roots(self):
        # It will work only for quadratic roots.
        # [0,0,0,a,b,c]
        roots = []
        if self.coef[0]==0 and self.coef[1]==0 and self.coef[2]==0:
            if self.coef[-3]!= 0:
                if ((self.coef[-2]**2)-(4*self.coef[-3]*self.coef[-1]))<0:
                    roots.append(complex(-self.coef[-2],math.sqrt(-((self.coef[-2]**2)-(4*self.coef[-3]*self.coef[-1]))))/(2*self.coef[-3]))
                    roots.append(complex(-self.coef[-2],-math.sqrt(-((self.coef[-2]**2)-(4*self.coef[-3]*self.coef[-1]))))/(2*self.coef[-3]))
                    return roots 
                else:
                    roots.append(((-self.coef[-2]) + math.sqrt((self.coef[-2]**2)-(4*self.coef[-3]*self.coef[-1])))/(2*self.coef[-3]))
                    roots.append(((-self.coef[-2]) - math.sqrt((self.coef[-2]**2)-(4*self.coef[-3]*self.coef[-1])))/(2*self.coef[-3]))
                    return roots
            else: # I'll just include the first degree equation.
                roots = []
                roots.append(-self.coef[-1] / self.coef[-2])
                return roots
        else:
            return "Order too high to solve for roots"
                
P1 = Polynomial([1, 2, 3])
P2 = Polynomial([100, 200])
print P1
print P1.__add__(P2)    # 1.0 z**2 + 102.0 z  + 203.0
print P1(1), P1(-1)     # 6.0 2.0
print (P1+P2)(10)       # 1323.0
print P1.__mul__(P1)    # 1.0 z**4 + 4.0 z**3 + 10.0 z**2 + 12.0 z  + 9.0
print (P1*P2) + P1      # 100.0 z**3 + 401.0 z**2 + 702.0 z  + 603.0
print P1.roots()        # ((-1+1.4142135623730951j), (-1-1.4142135623730951j))
print P2.roots()
P3 = Polynomial([3,2,-1]) # [-2.0]
print P3.roots()        # (0.3333333333333333, -1.0)
print (P1*P1).roots()   # Message.

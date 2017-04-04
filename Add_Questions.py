# Name: Soon Sam R Santos
# Date: February 15, 2017
# Session: 1
# Add_Questions.py

############ WK.1.4.3: List Comprehensions ###############

# Part1 - Even Squares
def evenSquares(list):
    new_list = [x**2 for x in list if x % 2 == 0]
    return new_list
# Test Cases
print evenSquares([1,2,3,4,5,6])   # 4, 16, 36

# Part2 - Sum of abs product
def sumAbsProd(list1, list2):
    # sumAbsProd ([2, -3],[4, -5])
    new_list = [abs(x*y) for x in list1 for y in list2]
    return sum(new_list)
# Test Cases
print sumAbsProd([2,-3],[4,-5])

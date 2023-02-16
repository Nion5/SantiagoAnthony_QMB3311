# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import math




##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


def CESutility_Valid(good_1: float, good_2: float, substitution_degree: float) -> float:
    """Return the constant elasticity of substition between good_1 and good_2 depending on thier substitution degree if all variables are positive

     >>> CESutility_Valid(4,5,2)
     6.40
     >>> CESutility_Valid(3,-6,5)
     None, good_2 is a negative value
     >>> CESutility_Valid(4,1,-2)
     None, substitution_degree is negatve
     """
    answer = (good_1**substitution_degree+good_2**substitution_degree)**(1/substitution_degree)

  
    if good_1<0:
        print("None ,good_1 is a negative value")
    elif good_2<0:
         print("None, good_2 is a negative value")
    elif good_1>0 and good_2>0 and substitution_degree>0:
         return answer
    else:
        print("None, substitution_degree is negatve")
    


# Exercise 2


def CESutility_in_budget(good_1: float, good_2: float, substitution_degree: float, basket_of_goods_1: float, basket_of_goods_2: float, wealth: float) -> float:
    """If basket of goods does not exceed wealt return the constant elasticity of substition between good_1 and good_2 depending on thier substitution degree if all variables are positive

     >>> CESutility_in_budget(4,5,2,2,4,7)
     6.40
     >>> CESutility_in_budget(3,6,5,3,3,3)
     None, basket of goods exceeds wealth
     >>> CESutility_in_budget(4,1,-2,1,1,5)
     None, substitution_degree is negatve
     """
    answer = (good_1**substitution_degree+good_2**substitution_degree)**(1/substitution_degree)

    if basket_of_goods_1<0:
          print("None, basket_of_good_1 is negative")
    elif basket_of_goods_2<0:
            print("None, basket_of_good_2 is negative")
    elif good_1<0:
        print("None ,good_1 is a negative value")
    elif good_2<0:
         print("None, good_2 is a negative value")
    elif basket_of_goods_1+basket_of_goods_2>wealth:
        print("None, basket of goods exceeds wealth")
    elif good_1>0 and good_2>0 and substitution_degree>0 and basket_of_goods_1+basket_of_goods_2<=wealth:
        return answer
    else:
        print("None, substitution_degree is negatve")
        
        

# Excercise 3


def logit (x:float,B0:float, B1:float)->float:
    """ Calculate the logit link function between variables
    
    >>>logit(1,2,3)
    0.99
    >>>logit(0.9,0.2,0.33)
    0.62
    >>>logit(0.85,0.45,1)
    0.79
    """
    answer = round((math.e**(B0+x*B1))/(1+math.e**(B0+x*B1)),2)
    
    return answer




# Execrcise 4


def logit_like (y:float,xi:float,B0:float, B1:float)->float:
    """ Calculate the logit link function or 1 minus the logit link funcition depending on the y variable
    
    >>>logit_like(1,0.9,0.2,0.33)
    0.62
    >>>logit_like(0,0.9,0.2,0.33)
    0.38
    >>>logit_like(0,0.85,0.45,1)
    0.21
    """
    answer = round((math.e**(B0+xi*B1))/(1+math.e**(B0+xi*B1)),2)
    
    if y>=1:
        return answer
    elif y<=0:
        return 1-answer
  

    
# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.

 print("#" + 50*"-")
 print("Testing my Examples for Exercise 1.")

 print("#" + 50*"-")
 print("Exercise 1, Example 1:")
 print("Evaluating CESutility_Valid(4,5,2)")
 print("Expected: " + str(6.40))
 print("Got: " + str(CESutility_Valid(4,5,2)))
 
 print("#" + 50*"-")
 print("Exercise 1, Example 2:")
 print("Evaluating CESutility_Valid(3,-6,5)")
 print("Expected: " + str("None, good_2 is a negative value"))
 print("Got: " + str(CESutility_Valid(3,-6,5)))


 print("#" + 50*"-")
 print("Exercise 2, Example 3:")
 print("Evaluating CESutility_Valid(4,1,-2)")
 print("Expected: " + str("None, substitution_degree is negatve"))
 print("Got: " + str(CESutility_Valid(4,1,-2)))
 
 
 
 
print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating CESutility_in_budget(4,5,2,2,4,7)")
print("Expected: " + str(6.40))
print("Got: " + str(CESutility_in_budget(4,5,2,2,4,7)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating CESutility_in_budget(3,6,5,3,3,3)")
print("Expected: " + str("None, basket of goods exceeds wealth"))
print("Got: " + str(CESutility_in_budget(3,6,5,3,3,3)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating CESutility_in_budget(4,1,-2,1,1,5)")
print("Expected: " + str("None, substitution_degree negatve"))
print("Got: " + str(CESutility_in_budget(4,1,-2,1,1,5)))




 print("#" + 50*"-")
 print("Testing my Examples for Exercise 3.")

 print("#" + 50*"-")
 print("Exercise 3, Example 1:")
 print("Evaluating logit(1,2,3)")
 print("Expected: " + str("0,99"))
 print("Got: " + str(logit(1,2,3)))
 
 print("#" + 50*"-")
 print("Exercise 3, Example 2:")
 print("Evaluating logit(0.9,0.2,0.33)")
 print("Expected: " + str("0.62"))
 print("Got: " + str(logit(0.9,0.2,0.33)))


 print("#" + 50*"-")
 print("Exercise 3, Example 3:")
 print("Evaluating logit(0.85,0.45,1)")
 print("Expected: " + str("0.79"))
 print("Got: " + str(logit(0.85,0.45,1)))
 
 
 
 print("#" + 50*"-")
 print("Testing my Examples for Exercise 4.")

 print("#" + 50*"-")
 print("Exercise 4, Example 1:")
 print("Evaluating logit_like(1,0.9,0.2,0.33)")
 print("Expected: " + str("0.62"))
 print("Got: " + str(logit_like(1,0.9,0.2,0.33)))
 
 print("#" + 50*"-")
 print("Exercise 4, Example 2:")
 print("Evaluating logit_like(0,0.9,0.2,0.33)")
 print("Expected: " + str("0.38"))
 print("Got: " + str(logit_like(0,0.9,0.2,0.33)))


 print("#" + 50*"-")
 print("Exercise 4 Example 3:")
 print("Evaluating logit_like(0,0.85,0.45,1)")
 print("Expected: " + str("0.21"))
 print("Got: " + str(logit_like(0,0.85,0.45,1)))

##################################################
# End
##################################################
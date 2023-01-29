# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Anthony Santiago
#
# Date: 01/29/2023
#
##################################################
#
# Sample Script for Assignment 2:
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################

# Exercise 1

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    100.0
    >>> next example goes here
    """
    answer = round(cash_flow/(1+interest_rate)**num_yrs,2)

    return answer



# Exercise 2

def Future_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the future value of cash_flow expected num_yrs from now
    discounted at interest_rate.

     >>> Future_value(100, 0.10, 1)
     110.0
     >>> Future_value(100, 0.10, 2)
     121.0
     >>> Future_value(115.74,0.20,3)
     200
     """
    answer = round(cash_flow*(1+interest_rate)**num_yrs,2)
     
    return answer

# Exercise 3

def Total_revenue(units_sold: float, selling_price: float) -> float:
    """Return the total revenue by multiplying units_sold and slelling_price

     >>> Total_revenue(200,2.00)
     400
     >>> Total_revenue(500,5.00)
     2500
     >>> Total_revenue(1000,7.00)
     7000
     """
    answer = round(units_sold*selling_price,2)
     
    return answer

# Exercise 4

def Total_cost(units_produced: float, fixed_cost: float, constant: float) -> float:
    """Return the total cost of units_produced squared plus fixed_cost

     >>> Total_cost(100,80,2.00)
     20080
     >>> Total_cost(50,45,3.00)
     7545
     >>> Total_cost(90,20,5.00)
     40520
     """
    answer = round(constant*units_produced**2+fixed_cost,2)

    return answer


# Exercise 5

def CESutility(good_1: float, good_2: float, substitution_degree: float) -> float:
    """Return the constant elasticity of substition between good_1 and good_2 depending on thier substitution degree

     >>> CESutility(4,5,2)
     6.40
     >>> CESutility(3,6,5)
     6.04
     >>> CESutility(4,1,2)
     4.12
     """
    answer = round((good_1**substitution_degree+good_2**substitution_degree)**(1/substitution_degree),2)

    return answer







##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results.


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating present_value(110, 0.10, 1)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(110, 0.10, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating present_value(121, 0.10, 2)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(121, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating Future_value(115.74, 0.20, 3)")
print("Expected: " + str(200.0))
print("Got: " + str(Future_value(115.74, 0.20, 3)))



print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating Future_value(100, 0.10, 1)")
print("Expected: " + str(110.0))
print("Got: " + str(Future_value(100, 0.10, 1)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating Future_value(100, 0.10, 2)")
print("Expected: " + str(121.0))
print("Got: " + str(Future_value(100, 0.10, 2)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating Future_value(115.74, 0.20, 3)")
print("Expected: " + str(200.0))
print("Got: " + str(Future_value(115.74, 0.20, 3)))




print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating Total_revenue(200,2.00)")
print("Expected: " + str(400.0))
print("Got: " + str(Total_revenue(200,2.00)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating Total_revenue(500,5.00)")
print("Expected: " + str(2500.0))
print("Got: " + str(Total_revenue(500,5.00)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating Total_revenue(1000,7.00)")
print("Expected: " + str(7000.0))
print("Got: " + str(Total_revenue(1000,7.00)))



print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating Total_cost(100,80,2.00)")
print("Expected: " + str(20080.0))
print("Got: " + str(Total_cost(100,80,2.00)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating Total_cost(50,45,3.00)")
print("Expected: " + str(7545.0))
print("Got: " + str(Total_cost(50,45,3.00)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating Total_cost(90,20,5.00)")
print("Expected: " + str(40520.0))
print("Got: " + str(Total_cost(90,20,5.00)))



print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating CESutility(4,5,2)")
print("Expected: " + str(6.40))
print("Got: " + str(CESutility(4,5,2)))


print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Evaluating CESutility(3,6,5))")
print("Expected: " + str(6.04))
print("Got: " + str(CESutility(3,6,5)))


print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Evaluating CESutility(4,5,2)")
print("Expected: " + str(4.12))
print("Got: " + str(CESutility(4,1,2)))



# ...


# Continue with the rest of your examples.
# Test all functions with three examples each.

# Choose good examples that will test interesting cases.
# Make sure they all work correctly.


##################################################
# End
##################################################

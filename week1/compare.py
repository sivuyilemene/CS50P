# Comparison operators
""" 
Operator	    Name	                  Example
__________________________________________________ 
# ==	    | Equal	                  | x == y	
# !=	    | Not equal	              | x != y	
# >	        | Greater than    	      | x > y	
# <	        | Less than	              | x < y	
# >=	    | Greater than or equal to| x  >= y	
# <=	    | Less than or equal to   | x <= y  

"""
# If elif else
x = int(input('whats x? '))
y = int(input('whats y? '))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
# OR
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# NOT EQUAL TO
if x != y:
    print("x is not equal to y")
else: 
    print("x is equal to y")


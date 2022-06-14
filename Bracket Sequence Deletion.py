# Importing required libraries
import math

# For loop for taking the inputs from the user
for _ in range(int(input())):
    n = int(input())
    string = input()
    
    # Initializing variables and setting them to default
    c = 0
    r = 0
    i = 0

    # While loop for the iteration within the string
    while i < n:
        # If the string is starting with a '('
        if string[i] == "(":
            if i == n - 1:
                i += 1
                r += 1
            else:
                c += 1
                i += 2

        # If the string is starting with a ')'        
        else:
            f = 0 # Flag Counter

            for j in range(i + 1, n):
                if string[j] == ")":
                    f += 1
                    c += 1
                    i = j + 1
                    break

            # If the flag is zero        
            if f == 0:
                r = n - i
                break

    # Print Statement            
    print(c, r)
            
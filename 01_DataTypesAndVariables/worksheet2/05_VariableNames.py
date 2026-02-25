"""
How does Python treat variable names that have the same value but are of different data types?
For example, what is the result of 3 == 3.0 and 3 is 3.0?
"""
3==3.0 true (value equality)
3 is 3.0 (is checks identity)it checks both objects are stored in the same memory location 
3(int) and 3.0 (float) are different objects.

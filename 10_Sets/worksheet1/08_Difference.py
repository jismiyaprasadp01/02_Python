"""
Python program to find the difference between two lists
Story: What games do you want to play this week that you didn't play last week?
Sample Input
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
Sample Output:
1
["jump", "run"]
"""

a= ["hide", "seek", "tag"]
b= ["hide", "seek", "jump", "run"]
diff=set(b)-set(a)
print(diff)

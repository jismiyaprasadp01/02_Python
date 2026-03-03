'''Erase the Forbidden Spells
You have a dictionary of spells, but some spells are now forbidden. 
Given a list of banned spell names, wipe them from your magic book!
Input: spells = {'fireball': 5, 'healing': 10, 'curse': 2}, banned = ['curse', 'fireball']
Expected Output: {'healing': 10}'''
import ast
spells=input("Enter the spells details:")
spells=ast.literal_eval(spells)

banned=input("Enter the banned spell details:")
banned=ast.literal_eval(banned)

for i in banned:
    if i in spells.keys():
        del(spells[i])

print("After deleting banned spells:",spells)

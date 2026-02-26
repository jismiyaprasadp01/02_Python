'''Write a recursive function sum_list(lst) to return the sum of all elements in a list'''
def sum_list(l):
    if not l:
        return 0
    return l[0]+sum_list(l[1:])

n = input("Enter numbers separated by spaces: ")
l = list(map(int, n.split()))
print("List:", l)
print(f"The sum of list :{sum_list(l)}")

#Check if Two Strings are Rotationally Equivalent

def rotationally_equivalent(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

str1 = "abcde"
str2 = "cdeab"
result = rotationally_equivalent(str1, str2)

print("Rotationally equivalent: Yes" if result else "Rotationally equivalent: No")

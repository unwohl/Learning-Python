import re

# Define my own character class:
#pattern0 = r"[aeiou]"

#if re.search(pattern0, "grey"):
    #print("match 1")
#if re.search(pattern0, "qwertyuiop"):
    #print("match 2")
#if re.search(pattern0, "rythmRytm"):
    #print("match 3")

# Define my own character class (Extension):
pattern01 = r"[A-Z][A-Z][0-9]"

if re.search(pattern01, "LS6"):
    print("match 1")
if re.search(pattern01, "LA"):
    print("match 2")
if re.search(pattern01, "Z"):
    print("match 3")



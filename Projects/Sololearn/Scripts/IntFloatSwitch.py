def switch(arg1):
    if isint(arg1):
        return float(arg1)
    else:
        return float_to_int(arg1)

def isint(arg1):
    arg_as_string = str(arg1)
    for i in arg_as_string:
        if i == ".":
            return False
    return True

def float_to_int(arg1):
    arg_as_string = str(arg1)
    c = 0
    empty_string = ""
    for i in arg_as_string:
       c += 1
       if i == ".":
           print(arg_as_string[c])
           break
    for i in range(c-1):
        empty_string += arg_as_string[i]
    if int(arg_as_string[c]) < 5:
        return int(empty_string)
    else:
        return int(empty_string) + 1

while(True):
    inp = input("gib ")
    print(switch(inp))



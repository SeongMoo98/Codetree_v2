inputs = input()
s = []

def check(inputs, s):
    for c in inputs:
        if c == '(':
            s.append(c)
            continue
        if c == ')':
            if len(s) == 0:
                return "No"
            s.pop()
   
    if len(s) == 0:
        return "Yes"
    else:
        return "No"

print(check(inputs, s))        

        
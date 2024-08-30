def isValid(s: str) -> bool:
    open = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            open.append(c)
        else:
            popped = open.pop() if len(open) > 0 else 'nah'
            if (c == ')' and popped != '(') or (c == ']' and popped != '[') or (c == '}' and popped != '{'):
                return False 
            
    if len(open) > 0:
        return False
    else:
        return True

print(isValid("()"))

'''
def isValid(s: str) -> bool:
    open = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c == '(' or c == '[' or c == '{':
            open.append(c)
        else:
            popped = open.pop() if len(open) > 0 else 'nah'
            if bracket_map[c] != popped:
                return False 
            
    if len(open) > 0:
        return False
    else:
        return True
'''
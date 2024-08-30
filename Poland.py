from typing import List
import math

def is_num(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def evalRPN(tokens: List[str]) -> int:
    stack = []
    index = 0
    
    while(index < len(tokens)) :
        print("Index: {} {}".format(index, stack))
        if not is_num(tokens[index]):
            value = stack.pop()
            if tokens[index] == '+':
                stack[-1] += value
            elif tokens[index] == '-':
                stack[-1] -= value
            elif tokens[index] == '*':
                stack[-1] *= value
            elif tokens[index] == '/':
                stack[-1] /= value
                stack[-1] = int(stack[-1])
        else:   
            stack.append(int(tokens[index]))
        index += 1

    return int(stack[0])
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))

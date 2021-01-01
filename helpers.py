import re

class Stack:
    def __init__(self):
        self.contents = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, data):
        self.contents.append(data)
        self.length += 1

    def pop(self):
        popped_value = None
        if self.length > 0:
            popped_value = self.contents.pop()
            self.length -= 1
        return popped_value

    def print_stack(self):
        arr = self.contents
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i])

def solve_prefix(expression, operators = ["+", "-", "*", "/"]):
    left_stack = Stack() # To hold operators
    right_stack = Stack() # To hold operands
    exp_array = expression.split(" ")

    if len(exp_array) % 2 == 0: # A valid postfix expression must at least contain odd number of inputs
        return None

    for i in range(len(exp_array)):
        if operators.count(exp_array[i]) == 1:
            left_stack.push(exp_array[i])
        elif operators.count(exp_array[i]) == 0 and re.match("[-|+]*[0-9]+", exp_array[i]):
            right_stack.push(int(exp_array[i]))
        
        if right_stack.length == 2 and left_stack.is_empty() == False:
            a = right_stack.pop()
            b = right_stack.pop()
            c = left_stack.pop()
            d = None
            if c == "+":
                d = b + a
            elif c == "-":
                d = b - a
            elif c == "*":
                d = b * a
            elif c == "/":
                d = round((b / a))

            right_stack.push(d)
        
    
    if left_stack.is_empty() and right_stack.length == 1: # Successful solution will leave no operators behind and have only one value
        return right_stack.pop()
    else:
        return None



# Graph Generator from tuple range (O(nm))
def generate_graph(range1, range2):
    my_graph = []
    for i in range(range1[0], range1[1]):
        for j in range(range2[0], range2[1]):
            my_graph.append((i, j))
    return my_graph

# Array Generator fron tuple range (O(n))
def generate_array(range1):
    my_array = []
    for i in range(range1[0], range1[1]):
        my_array.append(i)
    return my_array



if __name__ == "__main__":
    import sys
    expression = input("Enter prefix expression without variables: ")
    print(solve_prefix(expression))
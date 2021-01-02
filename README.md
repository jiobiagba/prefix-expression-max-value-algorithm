# Prefix Expression's Maximum Value Algorithm
This project is my solution to the challenge to **_get the maximum value of a prefix expression with at most 2 variables provided._**

# Motivation
After getting and attempting this challenge during my assessment for a developer role with a London company, I got  mail on the 29th of December that my solution had not passed enough edge cases to be considered for the next stage of the process.

It was a sad one for me as I really looked forward to working for the company but in the pain, I chose the solve the problem again with the details of it I could remember. Interestingly, this challenge had me learn Python in 3 days and for that alone, I am grateful.

# Background
A prefix expression is a mathematical expression that has operators first on the left before operands follow. When used, one advantage is that brackets do not need to be used to show operation order. For example, `(21 + 24) * 10` - an infix expression - becomes `* + 21 24 10` in prefix expression notation.

This challenge is to get the **maximum value of a prefix expression** which can have **at most 2 variables.** The rules or usage guide are as shown below:
1. Two inputs are provided. One is the expression and the second is the dictionary containing the range of values for the variables in the expression. For example, expression: `* 34 x` and variable: `{"x": (0,11)}`
2. When a range of value is provided in the variable dictionary, the end value is ignored. That is, `(0,11)` means `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
3. If there are no variables in the expression, an empty dictionary `{}` is supplied as the variable.
4. **The maximum number of variables permitted in an expression is 2**. A typical case with 2 variables will look like this - Expression: `* / + * 24 8 k -9 m` , Variable: `{"k": (1, 11), "m": (-10, 11)}`
5. **_Operands and operators in the expression MUST be separated by single space while negative numbers should be inserted by having the negtive sign close to the associated number without space as shown in 4._**

# Solution Process and Files
1. helpers.py
  * An helper function exists that can solve a prefix expression with no variables. This uses 2 stacks to hold the operators and operands separately. The beauty of this approach is that _this function can also solve a postfix expression_
  * When one variable is provided, another helper function generates an array from it. Values in this array are then substituted one after the other into the expression to get the maximum value
  * When two variables are provided, an helper function generates pairs of values akin to the edges of a graph (as the possible maximum values can be thought of like **_an Adjacency Matrix for Graphs_**). Each pair of values is then substituted to get the maximum value
2. index.py
  * All helper functions are imported here and the main logic for solving the problem is coded here.
  
# Tech/Languages
* Python
* MyPy Linter
Visual Studio Code as IDE

# Prerequisites
Before usage, do ensure the following are installed on your system
* Python 3.5 and above
* An appropriate Python Intepreter
* A Python Linter (optional)

# Installation
1. `git clone https://github.com/jiobiagba/prefix-expression-max-value-algorithm`
2. `cd prefix-expression-max-value-algorithm`
3. Run `python index.py` in your terminal

# Contribution
Contributions are welcome. Kindly check if the issue you intend raising has not been attended to in the past.If it hasn't, please feel free to raise a new [issue](https://github.com/jiobiagba/prefix-expression-max-value-algorithm/issues).

Please note that pull requests are also welcome but PRs made directly to the master branch are discouraged. Also please make it easy to understand what you are trying to address by specifying:
* the problem
* your operating system and 
* your python version
* your python intepreter and/or linter

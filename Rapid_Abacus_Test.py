import random

Operators = ["+", "-","/","*"]
Min_Operand = 4
Max_Operand =111
Total_Problems = 10

def generate_problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    operator = random.choice(Operators)
    
    expr = str(left) +" "+ operator + " " + str(right)
    answer =eval(expr)
    
    return expr, answer

for i in range(Total_Problems):
    expr, answer =generate_problem()
    while True:
        guess = input(" Problem #" +str(i+1)+ ": "+expr + " = ")
        if guess == str(answer):
            break
        
    

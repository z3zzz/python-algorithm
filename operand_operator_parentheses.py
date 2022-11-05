from itertools import permutations

def solution(expression):
    combinations = list(permutations(['*', '+', '-']))
    
    values = []
    for comb in combinations:
        op1 = comb[0]
        op2 = comb[1]
        
        temp_list = []
        for partial in expression.split(op1):
            temp = [f"({part})" for part in partial.split(op2)]
            temp_list.append(f"({op2.join(temp)})")

        final_expression = op1.join(temp_list)
        values.append(abs(eval(final_expression)))
        
    return max(values)








print(solution("100-200*300-500+20"))

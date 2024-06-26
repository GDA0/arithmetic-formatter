def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    operators = []
    second_operands = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first_operand, operator, second_operand = parts
        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
        
        if display_answers:
            result = str(int(first_operand) + int(second_operand)) if operator == "+" else str(int(first_operand) - int(second_operand))
            results.append(result)
    
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""
    
    for first, op, second in zip(first_operands, operators, second_operands):
        width = max(len(first), len(second)) + 2
        first_line += first.rjust(width) + "    "
        second_line += op + second.rjust(width - 1) + "    "
        dash_line += "-" * width + "    "
        
    if display_answers:
        for result in results:
            width = max(len(first_operands[results.index(result)]), len(second_operands[results.index(result)])) + 2
            result_line += result.rjust(width) + "    "
    
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()
    if display_answers:
        arranged_problems += "\n" + result_line.rstrip()
    
    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
import re


def arithmetic_arranger(problems, solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_value_output = ''
    second_value_output = ''
    separator_output = ''
    result_output = ''

    for problem in problems:
        if re.search('[/*]', problem):
            return "Error: Operator must be '+' or '-'."

        if re.search('[a-z]', problem, flags=re.IGNORECASE):
            return "Error: Numbers must only contain digits."

        problem = problem.split()
        if len(problem[0]) >= 5 or len(problem[2]) >= 5:
            return "Error: Numbers cannot be more than four digits."

        first_value = int(problem[0])
        second_value = int(problem[2])
        operator = problem[1]
        # Define how many '-' are needed:
        problem_length = max(len(problem[0]) + 2, len(problem[1]) + len(problem[2]) + 1)
        separator = problem_length * '-'

        if operator == '+':
            result = first_value + second_value
        else:
            result = first_value - second_value
            # 'eval()': evaluates JavaScript code represented as a string and returns a result.
            #           Executing JavaScript from a string is an enormous security risk.
            #           ' result = eval(f'{first_value}{operator}{second_value}') '

        first_value_output += str(first_value).rjust(problem_length) + "    "
        second_value_output += operator.ljust(1) + str(second_value).rjust(problem_length - 1) + "    "
        separator_output += separator + "    "
        result_output += str(result).rjust(problem_length) + "    "

        # String format() method:
        if solution:
            arranged_problems = '{0}\n{1}\n{2}\n{3}'.format(
                first_value_output.rstrip(),
                second_value_output.rstrip(),
                separator_output.rstrip(),
                result_output.rstrip()
            )
        else:
            arranged_problems = '{0}\n{1}\n{2}'.format(
                first_value_output.rstrip(),
                second_value_output.rstrip(),
                separator_output.rstrip()
            )

    return arranged_problems

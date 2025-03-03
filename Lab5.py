# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                result += "*"
            else:
                result += " "
        result += "\n"
    return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j) + ""
        result += "\n"
  
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = ""
    result = (n * (n +1)) / 2

    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(1, n + 1):
        for j in range(1, (n + 1) - i):
            result += " "
        for j in range(1, (2 * i)):
            result += "*"
        result += "\n"

    return result.rstrip()
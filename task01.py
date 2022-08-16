# 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
#                 Python example:
#                 def isEven(value):return value%2==0


# work wich string, it's faster on even, but slower on odd
def parity(num):
    i = ['1','3','5','7','9']
    return str(num)[-1] in i

if __name__ == '__main__':
    print(parity(55))

# true 'even'
# 6.599999999995498e-08 -- work wich str
# 6.400000000003625e-08 -- work wich %

# false 'odd'
# 6.299999999993811e-08 -- work wich str
# 6.499999999999562e-08 -- work wich %

import timeit

code_to_test = """
def parity(num):
    i = ['1','3','5','7','9']
    return str(num)[-1] in i
    
if __name__ == '__main__':
    print(parity(55))
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)






import re
def format(equation):
    equation.replace(' ', '')
    equation.replace('+-', '-')
    equation.replace('--', '+')
    return equation


def count_(equation):
    while re.search('\d[*/]\d', equation):
        equation_min = re.search('\d[*/]\d', equation).group()
        if equation_min.count('*'):
            num1,num2 =equation_min.split('*')
            equation_min_value = str(int(num1)*int(num2))
            equation = equation.replace(equation_min, equation_min_value)
        if equation_min.count('/'):
            num1, num2 = equation_min.split('/')
            equation_min_value = str(int(num1) / int(num2))
            equation = equation.replace(equation_min, equation_min_value)
    while re.search('\d[+-]\d', equation):#
        equation_max = re.search('\d[+-]\d', equation).group()
        if equation_max.count('+'):
            num3, num4= equation_max.split('+')
            equation_max_value = str(int(num3) + int(num4))
            equation = equation.replace(equation_max, equation_max_value)
        if equation_max.count('-'):
            num3, num4 = equation_max.split('-')
            equation_max_value = str(int(num3) - int(num4))
            equation = equation.replace(equation_max, equation_max_value)
    return equation


def choose(equation_):#选出括号
    while re.search('\([^()]+\)', equation_):
        equation_1 = re.search('\([^()]+\)', equation_).group()
        equation_1 = equation_1[1:-1]
        equation_2 = count_(equation_1)
        equation_ = equation_.replace(equation_1, equation_2)
        return equation_
if __name__ == '__main__':
    equation = input('请输入你想计算的算式>>:').strip()  ##(12+41*())
    if equation.count('(') != equation.count(')'):
        print('输入有误')
        exit(0)
    else:
        equation = format(equation)
        if equation.count('(')==0:
            value = count_(equation)
            print()
        if equation.count('(') != 0:
            equation_new = choose(equation)
            value = count_(equation_new)
            print(value)





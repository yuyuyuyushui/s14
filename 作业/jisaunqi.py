import re


def settle(equation_str):#格式化算式

    flag1 = True
    while flag1:
        try:
            equation_str1 = re.search(' ', equation_str).group()
            equation_str = equation_str.replace(equation_str1, '')
        except AttributeError:
            flag1 = False
    flag2 = True
    while flag2:
        try:
            equation_str1 = re.search('\+-', equation_str).group()
            equation_str = equation_str.replace(equation_str1, '-')
        except AttributeError:
            flag2 = False
    return equation_str


def choose(equation_):#选出括号
    equation_1 = re.search('\([^()]+\)', equation_).group()
    return equation_1

def count(equation):#计算加减
    flag = True
    while flag:
        try:
            equation_cheng = re.search('\d[*/]\d', equation).group()
            equation_cheng
        except AttributeError:
            try:
                re.search('\d[+-]\d', equation).group()
            except AttributeError:
                return equation_jie

if __name__ == '__main__':
    equation = input('请输入你想计算的算式>>:').strip()  ##(12+41*())
    new_equation = settle(equation)
    flag = True
    while flag:
        try:
            new_equation_1 = choose(new_equation)  # 选出括号
            new_equation_2 = new_equation_1[1:-1]  # 去掉括号
            new_equation_2 = count(new_equation_2)
            new_equation = new_equation.replace(new_equation_1, new_equation_2)
            new_equation = settle(new_equation)
        except AttributeError:
            count(new_equation)



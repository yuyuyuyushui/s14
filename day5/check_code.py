import random

check_code = ''
for i in range(4):

    if i == 1 or i == 2:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
        print(tmp)

    check_code += str(tmp)

print(check_code)

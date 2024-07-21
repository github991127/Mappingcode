from sympy import pi, EulerGamma, E

N = 30


class mappingcode:
    def __init__(self):
        π = pi.evalf(N)  # 得到N位小数位的π
        γ = EulerGamma.evalf(N)
        e = E.evalf(N)


def calculator(a, b, c):
    # 圆周率数π，自然底数e，欧拉常数γ
    π = pi.evalf(N)  # 得到N位小数位的π
    γ = EulerGamma.evalf(N)
    e = E.evalf(N)
    formula = 'a*π+b*e+c*γ'
    # formula = input('请输入要计算的式子:')
    return eval(formula)


def mapping(x):
    str_dem = '0123456789'
    list_index = []
    x = str(x)
    index = x.find('.')
    x = x[index + 1:]  # 获取小数点后的数字，存取为字符串
    # print(x)
    for dem in str_dem:
        index = x.find(dem) + 1
        list_index.append(index)
    return list_index


def mappingcode(a, b, c):
    list_index = [0]
    global N
    N = 30
    while 0 in list_index:
        x = calculator(a, b, c)
        if x == 0:
            formula = str(a) + '*π+' + str(b) + '*e+' + str(c) + '*γ'
            return formula, x, list_index
        list_index = mapping(x)
        N = N + 10
    formula = str(a) + '*π+' + str(b) + '*e+' + str(c) + '*γ'
    return formula, x, list_index


if __name__ == '__main__':
    a = 0
    b = c = 1.1
    formula, x, list_index = mappingcode(a, b, c)
    print(formula, '=', x)
    print(list_index)
    # for i in range(len(list_index)):
    #     print(i,'↔',list_index[i])

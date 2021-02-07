import matplotlib

matplotlib.use("template")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import math
import sys


def init(n):
    params = []
    for i in range(n + 1):
        x = float(input("{} коефіцієент рівняння: ").format(i + 1))
        params.append(x)
    return params


def f(param, x):
    y = 0
    for i in range(len(param)):
        y = param[i] * math.pow(x, i) + y
    return y


def dx(param, x):
    return abs(f(param, x))


def df(param, x):
    y = 0
    for i in range(1, len(param), 1):
        y = y + (i * param[i] * math.pow(x, i))
    return y


def ddf(param, x):
    y = 0
    for i in range(2, len(param), 1):
        y = y + (i * (i - 1) * param[i] * math.pow(x, i))
    return y


def decomp(param, p, q, eps):
    intervals = []
    i = p
    t = 10.0 * eps
    while i < q:
        if f(param, i) * f(param, i + t) < 0:
            t = t / 10
            i = i + t
        else:
            i = i + t
            if t < eps:
                intervals.append([i - 3 * t, i + 3 * t])
                if len(intervals) == 2:
                    break
                t = 10 * eps
    return intervals


def printfunc(param):
    string = ''
    for i in range(len(param)):
        string = string + "+ {}x^{}".format(param[i], i)
    return string


# Виконана перевірка

def newtonRaphson(l, r, eps, param):
    condition = True
    x0 = (l + r) / 2.0
    while condition:
        x1 = x0 - f(param, x0) / df(param, x0)
        if abs(x1 - x0) < eps:
            condition = False
        else:
            x0 = x1
    return x1


def samesign(a, b):
    return a * b > 0


def Bisect(fx, l, r, eps, param):
    step = 0
    while True:
        midpoint = (l + r) / 2.0
        if samesign(fx(param, l), fx(param, midpoint)):
            l = midpoint
        else:
            r = midpoint
        if dx(param, midpoint) < eps:
            break
        step = step + 1
    return midpoint


########################
# проблемнв зона
def simplefleft(param, x):
    return f(param, x) - param[1] * x


def simpleIterationMethod(l, eps, param):
    condition = True
    x0 = l
    while condition:
        if param[1] != 0:
            x1 = simplefleft(param, x0) / -param[1]
        else:
            x1 = simplefleft(param, x0)
        if abs(x1 - x0) < eps:
            condition = False
        x0 = x1
    return x1


########################
def secantMethod(l, r, eps, param):
    x1 = (l + r) / 2.0
    x2 = f(param, x1)
    iterate = 0
    maxIteration = 100
    cond = True
    while cond and iterate < maxIteration:
        y1 = x2 - ((f(param, x2) * (x2 - x1)) / (f(param, x2) - f(param, x1)))
        if abs(y1 - x2) < eps:
            cond = False
        x1 = x2
        x2 = y1
        iterate += 1
    return x1


def steffencenMethod(l, r, eps, param):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = x0 - ((f(param, x0) ** 2) / (f(param, x0 + f(param, x0)) - f(param, x0)))
        if abs(x0 - x1) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def easeNewtomRaphsonMethod(l, r, eps, param):
    iterate = 0
    maxIteration = 100
    x0 = (l + r) / 2.0
    j = x0
    cond = True
    while cond and iterate < maxIteration:
        x1 = x0 - (f(param, x0) / df(param, j))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def modifiedNewtonRaphsonMethod(l, r, eps, param, m=1):
    condition = True
    x0 = (l + r) / 2.0
    while condition:
        x1 = x0 - m * (f(param, x0) / df(param, x0))
        if abs(x1 - x0) < eps:
            condition = False
        else:
            x0 = x1
    return x1


def HeiliMethod(l, r, eps, param):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = x0 - ((f(param, x0) * df(param, x0)) / (math.pow(df(param, x0), 2) - (f(param, x0) * ddf(param, x0))))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def extendNewtonMethod(l, r, eps, param):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = newtonRaphson(l, r, eps, param) - (
                (ddf(param, x0) * math.pow(f(param, x0), 2)) / (2 * math.pow(df(param, x0), 2)))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def interpolationMethod(l, r, eps, param):
    x1 = (l + r) / 2.0
    x2 = f(param, x1)
    iterate = 0
    maxIteration = 100
    cond = True
    while cond and iterate < maxIteration:
        y1 = x2 - ((f(param, x2) * (x2 - x1)) / (f(param, x2) - f(param, x1)))
        if abs(y1 - x2) < eps:
            cond = False
        x1 = x2
        x2 = y1
        iterate += 1
    return x1


def subNewtonMethod(l, r, eps, param):
    h0 = 1
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        hk = 0.5 * h0
        x1 = x0 - ((hk * f(param, x0)) / (f(param, x0 + hk) - f(param, x0)))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        h0 = hk
    return x1


def XAxis(a, b, x):
    return a * x + b


def YAxis(a, b, x):
    return b * x + a


class NoRootsFoundException:
    BaseException(Exception)


def main(f, param, num, eps):
    testroots = []
    intervals = decomp(param, -100, 100, eps)
    if num == 2:
        print("Метод половинного поділу")
        for i in range(len(intervals)):
            testroot = Bisect(f, intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 1:
        print("Метод Ньютона")
        for i in range(len(intervals)):
            testroot = newtonRaphson(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 3:
        print("Метод простої ітерації")
        for i in range(len(intervals)):
            testroot = simpleIterationMethod(intervals[i][0], eps, param)
            testroots.append(testroot)
    elif num == 4:
        print("Метод січних.")
        for i in range(len(intervals)):
            testroot = secantMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 6:
        print("Метод Ньютона(спрощений).")
        for i in range(len(intervals)):
            testroot = easeNewtomRaphsonMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 7:
        print("Метод Ньютона(модифікований).")
        for i in range(len(intervals)):
            testroot = modifiedNewtonRaphsonMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 8:
        print("Метод Хейлі.")
        for i in range(len(intervals)):
            testroot = HeiliMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 9:
        print("Метод Ньютона(розширений).")
        for i in range(len(intervals)):
            testroot = extendNewtonMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 10:
        print("Метод хорд.")
        for i in range(len(intervals)):
            testroot = interpolationMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 11:
        print("Метод Ньютона(різницевий).")
        for i in range(len(intervals)):
            testroot = subNewtonMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    elif num == 5:
        print("Метод Стеффенсена.")
        for i in range(len(intervals)):
            testroot = steffencenMethod(intervals[i][0], intervals[i][1], eps, param)
            testroots.append(testroot)
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-32, 32, 0.8)
    plt.plot(x, f(param, x))
    plt.plot(x, XAxis(0, 0, x))
    plt.plot(YAxis(0, 0, x), y)
    plt.savefig("static/img/plot.png")
    for i in range(len(testroots)):
        print(testroots[i])
    return testroots


if __name__ == '__main__':
    print("####################")
    print("1: Метод Ньютона. ")
    print("2: Метод половинного поділу. ")
    print("3: Метод простої ітерації. ")
    print("4: Метод січних. ")
    print("5: Метод Стеффенсена. ")
    print("6: Метод Ньютона(спрощений). ")
    print("7: Метод Ньютона(модифікований). ")
    print("8: Метод Хейлі. ")
    print("9: Метод Ньютона(розширений). ")
    print("10: Метод хорд. ")
    print("11: Метод Ньютона(різницевий). ")
    print("#########################")
    num = int(input("Введіть номер методу: "))
    n = int(input("Степінь рівняння: "))
    params = init(n)
    details = printfunc(params)
    eps = float(input("Точність: "))
    print("Рівняння: y = {}".format(details))
    main(f, params, num, eps)

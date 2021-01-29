import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def init():
    params = []
    n = 3
    for i in range(n):
        x = float(input("{} коефіцієент рівняння: ").format(i + 1))
        params.append(x)
    return params


def f(a, b, c, x):
    return a * x * x + b * x + c


def dx(a, b, c, x):
    return abs(f(a, b, c, x))


def df(a, b, x):
    if 2 * a * x + b != 0:
        return 2 * a * x + b
    else:
        return x


def ddf(a):
    return 2 * a


def decomp(a, b, c, p, q, eps):
    intervals = []
    i = p
    t = 10 * eps
    while i < q:
        if f(a, b, c, i) * f(a, b, c, i + t) < 0:
            t = t / 10
            i = i + t
        else:
            i = i + t
            if t < eps:
                intervals.append([i - 3 * t, i + 3 * t])
                t = 10 * eps
    return intervals


def printfunc(a, b, c):
    return "{}x^2 + {}x + {}".format(a, b, c)


# Виконана перевірка

def newtonRaphson(l, r, eps, a, b, c):
    condition = True
    x0 = (l + r) / 2.0
    while condition:
        x1 = x0 - f(a, b, c, x0) / df(a, b, x0)
        if abs(x1 - x0) < eps:
            condition = False
        else:
            x0 = x1
    return x1


def samesign(a, b):
    return a * b > 0


def Bisect(fx, l, r, eps, a, b, c):
    midpoint = 0
    step = 0
    while True:
        midpoint = (l + r) / 2.0
        if samesign(fx(a, b, c, l), fx(a, b, c, midpoint)):
            l = midpoint
        else:
            r = midpoint
        if dx(a, b, c, midpoint) < eps:
            break
        step = step + 1
    return midpoint


########################
# проблемнв зона
def simplefleft(a, c, x):
    return a * x * x + c


def simpleIterationMethod(l, r, eps, a, b, c):
    condition = True
    x0 = l
    while condition:
        if b != 0:
            x1 = simplefleft(a, c, x0) / -b
        else:
            x1 = simplefleft(a, c, x0)
        if abs(x1 - x0) < eps:
            condition = False
        x0 = x1
    return x1


########################
def secantMethod(l, r, eps, a, b, c):
    x1 = (l + r) / 2.0
    x2 = f(a, b, c, x1)
    iterate = 0
    maxIteration = 100
    cond = True
    while cond and iterate < maxIteration:
        y1 = x2 - ((f(a, b, c, x2) * (x2 - x1)) / ((f(a, b, c, x2) - f(a, b, c, x1))))
        if abs(y1 - x2) < eps:
            cond = False
        x1 = x2
        x2 = y1
        iterate += 1
    return x1


def steffencenMethod(l, r, eps, a, b, c):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = x0 - ((f(a, b, c, x0) ** 2) / (f(a, b, c, x0 + f(a, b, c, x0)) - f(a, b, c, x0)))
        if abs(x0 - x1) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def easeNewtomRaphsonMethod(l, r, eps, a, b, c):
    iterate = 0
    maxIteration = 100
    x0 = (l + r) / 2.0
    j = x0
    cond = True
    while cond and iterate < maxIteration:
        x1 = x0 - (f(a, b, c, x0) / df(a, b, j))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def modifiedNewtonRaphsonMethod(l, r, eps, a, b, c, m=1):
    condition = True
    x0 = (l + r) / 2.0
    while condition:
        x1 = x0 - m * (f(a, b, c, x0) / df(a, b, x0))
        if abs(x1 - x0) < eps:
            condition = False
        else:
            x0 = x1
    return x1


def HeiliMethod(l, r, eps, a, b, c):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = x0 - ((f(a, b, c, x0) * df(a, b, x0)) / (math.pow(df(a, b, x0), 2) - (f(a, b, c, x0) * ddf(a))))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def extendNewtonMethod(l, r, eps, a, b, c):
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        x1 = newtonRaphson(x0, eps, a, b, c) - (
                    (ddf(a) * math.pow(f(a, b, c, x0), 2)) / (2 * math.pow(df(a, b, x0), 2)))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        iterate += 1
    return x1


def interpolationMethod(l, r, eps, a, b, c):
    x1 = (l + r) / 2.0
    x2 = f(a, b, c, x1)
    iterate = 0
    maxIteration = 100
    cond = True
    while cond and iterate < maxIteration:
        y1 = x2 - ((f(a, b, c, x2) * (x2 - x1)) / ((f(a, b, c, x2) - f(a, b, c, x1))))
        if abs(y1 - x2) < eps:
            cond = False
        x1 = x2
        x2 = y1
        iterate += 1
    return x1


def subNewtonMethod(l, r, eps, a, b, c):
    h0 = 1
    iterate = 0
    maxIteration = 100
    cond = True
    x0 = (l + r) / 2.0
    while cond and iterate < maxIteration:
        hk = 0.5 * h0
        x1 = x0 - ((hk * f(a, b, c, x0)) / (f(a, b, c, x0 + hk) - f(a, b, c, x0)))
        if abs(x1 - x0) < eps:
            cond = False
        x0 = x1
        h0 = hk
    return x1


def XAxis(a, b, x):
    return a * x + b


def YAxis(a, b, x):
    return b * x + a


def main(f, a, b, c, num,eps):
    left, right = decomp(a, b, c, -100, 100, eps)
    if num == 2:
        print("Метод половинного поділу")
        testroot1 = Bisect(f, left[0], left[1], eps, a, b, c)
        testroot2 = Bisect(f, right[0], right[1], eps, a, b, c)
    elif num == 1:
        print("Метод Ньютона")
        testroot1 = newtonRaphson(left[0], left[1], eps, a, b, c)
        testroot2 = newtonRaphson(right[0], right[1], eps, a, b, c)
    elif num == 3:
        print("Метод простої ітерації")
        testroot1 = simpleIterationMethod(left[0], left[1], eps, a, b, c)
        testroot2 = simpleIterationMethod(right[0], right[1], eps, a, b, c)
    elif num == 4:
        print("Метод січних.")
        testroot1 = secantMethod(left[0], left[1], eps, a, b, c)
        testroot2 = secantMethod(right[0], right[1], eps, a, b, c)
    elif num == 6:
        print("Метод Ньютона(спрощений).")
        testroot1 = easeNewtomRaphsonMethod(left[0], left[1], eps, a, b, c)
        testroot2 = easeNewtomRaphsonMethod(right[0], right[1], eps, a, b, c)
    elif num == 7:
        print("Метод Ньютона(модифікований).")
        testroot1 = modifiedNewtonRaphsonMethod(left[0], left[1], eps, a, b, c)
        testroot2 = modifiedNewtonRaphsonMethod(right[0], right[1], eps, a, b, c)
    elif num == 8:
        print("Метод Хейлі.")
        testroot1 = HeiliMethod(left[0], left[1], eps, a, b, c)
        testroot2 = HeiliMethod(right[0], right[1], eps, a, b, c)
    elif num == 9:
        print("Метод Ньютона(розширений).")
        testroot1 = extendNewtonMethod(left[0], left[1], eps, a, b, c)
        testroot2 = extendNewtonMethod(right[0], right[1], eps, a, b, c)
    elif num == 10:
        print("Метод хорд.")
        testroot1 = interpolationMethod(left[0], left[1], eps, a, b, c)
        testroot2 = interpolationMethod(right[0], right[1], eps, a, b, c)
    elif num == 11:
        print("Метод Ньютона(різницевий).")
        testroot1 = subNewtonMethod(left[0], left[1], eps, a, b, c)
        testroot2 = subNewtonMethod(right[0], right[1], eps, a, b, c)
    elif num == 5:
        print("Метод Стеффенсена.")
        testroot1 = steffencenMethod(left[0], left[1], eps, a, b, c)
        testroot2 = steffencenMethod(right[0], right[1], eps, a, b, c)
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-32, 32, 0.8)
    plt.plot(x, f(a, b, c, x))
    plt.plot(x, XAxis(0, 0, x))
    plt.plot(YAxis(0, 0, x), y)
    plt.savefig("/static/img/plot,png")
    print(testroot1)
    print(testroot2)
    # print(left)
    # print(right)


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
    params = init()
    details = printfunc(params[0], params[1], params[2])
    print("Рівняння: y = {}".format(details))
    main(f, params[0], params[1], params[2], num)

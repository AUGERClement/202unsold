#!/bin/python3.7

from numpy import var

#a and b are prog arg, x and y are prices of elements sold
def proba(a, b, x, y):
    res = ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150))
    return res


def get_y_final(x_y_results):
    y_final = x_y_results[0].copy()
    i = 1
    j = 0

    while (i < len(x_y_results)):
        while (j < len(x_y_results[i])):
            y_final[j] += x_y_results[i][j]
            j += 1
        i += 1
        j = 0
    return y_final

def step_1(a, b):
    x_y_results = []
    z_results = {}
    i = 1
    j = 1
    tmp = 0
    key = 0

    while (i < 6):
        x_y_results.append([])
        while (j < 6):
            key = (i + j) * 10
            if (key not in z_results):
                z_results[key] = 0
            tmp = proba(a, b, i * 10, j * 10)
            x_y_results[i - 1].append(tmp)
            z_results[key] += tmp
            j += 1
        x_y_results[i - 1].append(sum(x_y_results[i - 1]))
        i += 1
        j = 1
    x_y_results.append(get_y_final(x_y_results))
    print_arr(x_y_results)
    return x_y_results, z_results

def print_arr(x_y_results):
    i = 0
    j = 0

    print("-----------------------------------------------------")
    print("", "X=10", "X=20", "X=30", "X=40", "X=50", "Y law", sep="\t")
    while (i < len(x_y_results)):
        print_Y(i)
        while (j < len(x_y_results[i])):
            print_value(x_y_results[j][i], i, j)
            j += 1
        i += 1
        j = 0
    print("-----------------------------------------------------")

def print_Y(i):
    if (i < 5):
        print("Y=", ((i + 1) * 10), "\t", sep="", end="")
    else:
        print("X law", end="\t")

def print_value(value, i, j):
    if (i == 5 and j == 5):
        print(1)
    elif (j == 5):
        print('%.3f' % value)
    else:
        print('%.3f' % value, end="\t")

def print_Z(z_results):
    print("z", end="\t")
    
    for key in z_results.keys():
        print(key, end="\t")
    print("total")
    print("p(Z=z)", end="\t")
    for value in z_results.values():
        print('%.03f' % value, end="\t")
    print(1)
    print("-----------------------------------------------------")
    return

def get_expected(Target, x_y_results):
    i = 0
    expected = 0.0

    while (i < len(x_y_results) - 1):
        if (Target == 'X'):
            expected += (i + 1) * 10 * x_y_results[i][5]
        elif (Target == 'Y'):
            expected += (i + 1) * 10 * x_y_results[5][i]
        i += 1
    return expected

def get_var(Target, x_y_results, expected_target):
    var = 0.0
    tmp = 0
    i = 0

    while (i < len(x_y_results) - 1):
        tmp = (i + 1) * 10
        if (Target == 'X'):
            var += (tmp - expected_target) * (tmp - expected_target) * x_y_results[i][5]
        elif (Target == 'Y'):
            var += (tmp - expected_target) * (tmp - expected_target) * x_y_results[5][i]
        i += 1
    return var

def step_3(x_y_results, z_results):
    expected_x = get_expected('X', x_y_results)
    var_x = get_var('X', x_y_results, expected_x)
    expected_y = get_expected('Y', x_y_results)
    var_y = get_var('Y', x_y_results, expected_y)
    expected_z = expected_x + expected_y
    var_z = var_x + var_y

    print("expected value of X:", '%0.1f' % expected_x, sep="\t")
    print("variance of X:\t", '%0.1f' % var_x, sep="\t")
    print("expected value of Y:", '%0.1f' % expected_y, sep="\t")
    print("variance of Y:\t", '%0.1f' % var_y, sep="\t")
    print("expected value of Z:", '%0.1f' % expected_z, sep="\t")
    print("variance of Z:\t", '%0.1f' % var_z, sep="\t")
    print("-----------------------------------------------------")
    return
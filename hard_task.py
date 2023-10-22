#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def shi(x, tolerance=1e-10):
    result = 0.0
    term = x
    n = 0

    while abs(term) > tolerance:
        result += term
        n += 1
        term *= (x * x) / ((2 * n + 1) * (2 * n))

    return result


if __name__ == "__main__":
    x = int(input())
    print(math.sinh(x))
    print(shi(x))

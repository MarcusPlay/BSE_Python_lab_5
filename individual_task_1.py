#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def total_price(price: float):
    if (price < 200):
        return price
    elif (200 <= price < 500):
        return price * 0.97
    elif (500 <= price < 800):
        return price * 0.95
    elif (800 <= price < 1000):
        return price * 0.93
    elif (1000 <= price):
        return price * 0.91


if __name__ == "__main__":
    x1 = int(input())
    x2 = int(input())

    print(total_price((8 * x1) + (2 * x2)))

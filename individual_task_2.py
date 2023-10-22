#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def find_point(point1, radius1, point2, radius2):
    if (math.fabs(point1 - point2) > (radius1 + radius2)):
        return 0
    elif (math.fabs(point1 - point2) == (radius1 + radius2)):
        return 1
    elif ((math.fabs(point1 - point2) < (radius1 + radius2)) and (math.fabs(point1 - point2) >= math.fabs(radius1 - radius2))):
        return 2
    elif (math.fabs(point1 - point2) < (math.fabs(radius1 - radius2))):
        return "∞"
    elif ((point1 == point2) and (radius1 == radius2)):
        return "∞"


if __name__ == "__main__":
    point1 = float(input())
    radius1 = float(input())
    point2 = float(input())
    radius2 = float(input())

    points = find_point(point1, radius1, point2, radius2)
    print(f"Эти две окружности имеют {points} точек перечения")
    input()

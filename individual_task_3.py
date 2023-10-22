#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def how_much(S):
    # 1, 2, 5, 10, 100, 500
    if S >= 500:
        print(f"500-{S // 500}шт", end='; ')
        S = S % 500
    if S >= 100:
        print(f"100-{S // 100}шт", end='; ')
        S = S % 100
    if S >= 10:
        print(f"10-{S // 10}шт", end='; ')
        S = S % 10
    if S >= 5:
        print(f"5-{S // 5}шт", end='; ')
        S = S % 5
    if S >= 2:
        print(f"2-{S // 2}шт", end='; ')
        S = S % 2
    if S >= 1:
        print(f"1-{S // 1}шт")
        S = S % 1


if __name__ == "__main__":
    S = int(input())
    how_much(S)

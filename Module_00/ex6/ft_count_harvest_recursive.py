#!/usr/bin/env python3

def ft_count_harvest_recursive():
    num_days = int(input("Days until harvest: "))
    funcion_helper(1, num_days)
    print("Harvest time! ")


def funcion_helper(current, end):
    if (current > end):
        return
    print("Day", current)
    funcion_helper(current + 1, end)

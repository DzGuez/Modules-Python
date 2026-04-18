#!/usr/bin/env python3

def ft_count_harvest_iterative():
    num_days = int(input("Days until harvest: "))
    for day in range(1, num_days + 1):
        print("Day", day)
    print("Harvest time! ")

#!/usr/bin/env python
# -*-coding: utf-8 -*-


def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data)//2]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num <= mid:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


a = quick_sort([1, 3, 2, 5, 5, 7, 2])
print(a)

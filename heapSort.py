#!/usr/bin/env python
# -*-coding: utf-8 -*-

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # left child
    if left < largest:

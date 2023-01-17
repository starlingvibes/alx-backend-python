#!/usr/bin/env python3

"""
Type-annotating complex types
"""


def sum_list(input_list: list[float, ...]) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)

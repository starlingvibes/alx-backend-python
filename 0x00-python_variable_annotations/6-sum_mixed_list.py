#!/usr/bin/env python3

"""
Annotating a complex type - mixed list
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats, returns value as float
    """
    return sum(mxd_lst)

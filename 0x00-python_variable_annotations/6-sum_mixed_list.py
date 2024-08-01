#!/usr/bin/env python3
"""
Complex types - mixed list
Returns their sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Typed-annotated function sum_mixed_list
    """
    return sum(mxd_lst)

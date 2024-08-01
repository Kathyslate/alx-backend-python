#!/usr/bin/env python3
"""
Type checking
Use mypy to validate code piece
apply any necessary changes
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return necessary changes
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
        ]
    return zoomed_in


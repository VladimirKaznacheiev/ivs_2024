"""
IVS Project 2 - Golden Calculator

@brief: This module provides profiling for Golden Calculator

@authors: Murad Mikogaziev (xmikog00)
@file profiling.py
@date 2024-24-04
"""

import cProfile
import math_logic as ml


def calculate_sample_std_deviation(nums):
    """Calculate the sample standard deviation of a list of numbers.

    Args:
        nums (list): List of numbers.

    Returns:
        float: The sample standard deviation.

    Raises:
        ValueError: If less than two numbers are provided.
    """
    n = len(nums)
    if n < 2:
        raise ValueError("At least two numbers are required for calculating sample standard deviation.")

    mean = ml.div(ml.plus(nums), n)
    variance = ml.div(ml.plus(ml.power(ml.minus(x, mean), 2) for x in nums), ml.minus(n, 1))
    std_deviation = ml.root(variance)
    return std_deviation


def read_input_numbers():
    """Read numbers from standard input.

    Returns:
        list: List of numbers read from input.
    """
    numbers = []
    try:
        for line in iter(input, ''):
            numbers.extend(map(float, line.split()))
    except EOFError:
        pass
    return numbers


if __name__ == '__main__':
    numbers = read_input_numbers()
    cProfile.run('calculate_sample_std_deviation(numbers)')

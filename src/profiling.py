import cProfile
import math_logic as ml


def calculate_sample_std_deviation(nums):
    n = len(nums)
    if n < 2:
        raise ValueError("At least two numbers are required for calculating sample standard deviation.")

    mean = ml.div(ml.plus(nums), n)
    variance = ml.div(ml.plus(ml.power(ml.minus(x, mean), 2) for x in nums), ml.minus(n, 1))
    std_deviation = ml.root(variance)
    return std_deviation


def read_input_numbers():
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

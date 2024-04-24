import cProfile
from math_logic import calculate_sample_std_deviation


def read_input_numbers():
    numbers = []
    # Read input numbers from standard input until EOF
    for line in iter(input, ''):
        numbers.extend(map(float, line.split()))
    return numbers


if __name__ == '__main__':
    # Read input numbers
    numbers = read_input_numbers()

    # Profile the calculation of sample standard deviation
    cProfile.run('calculate_sample_std_deviation(numbers)')
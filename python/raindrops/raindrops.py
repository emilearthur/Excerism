def convert(number):
    _factor = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = []

    factors = [i for i in range(3, 9, 2) if number % i == 0]

    if factors:
        for num in factors:
            for key, value in _factor.items():
                if key == num:
                    output.append(value)
        return ''.join(output)
    return str(number)

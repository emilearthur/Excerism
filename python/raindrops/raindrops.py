def convert(number):
    _factor = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = []

    for key, value in _factor.items():
        if number % key == 0:
            output.append(value)

    if output:
        return ''.join(output)
    return str(number)

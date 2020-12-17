def convert(number):
    _factor = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = []

    def factor(number_):
        for i in range(3, 9, 2):
            if number_ % i == 0:
                yield i

    if number:
        factor_output = factor(number)
        for i in factor_output:
            output.append(_factor.get(i))
        outputx = ''.join(output)
        if outputx:
            return outputx
        else:
            return str(number)

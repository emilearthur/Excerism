def convert(number):
    _factor = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = []

    def factor(number_):
        factor_out = []
        for i in range(3, 9, 2):
            if number_ % i == 0:
                factor_out.append(i)
        return factor_out

    if number:
        factor_output = factor(number)
        if factor_output:
            for i in factor_output:
                output.append(_factor.get(i))
            return ''.join(output)
        else:
            return str(number)

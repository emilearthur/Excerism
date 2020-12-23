def convert(number):
    _factor = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = []

    def factor(number_):
        for i in range(3, 9, 2):
            if number_ % i == 0:
                yield i

    if number:
        output = [_factor.get(i) for i in factor(number)]
        if output:
            return ''.join(output)
        return str(number)

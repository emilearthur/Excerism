def proteins(strand):
    outputs = []
    protein_dict = {
                    'AUG': 'Methionine',
                    'UUU': 'Phenylalanine',
                    'UUC': 'Phenylalanine',
                    'UUA': 'Leucine',
                    'UUG': 'Leucine',
                    'UCU': 'Serine',
                    'UCC': 'Serine',
                    'UCA': 'Serine',
                    'UCG': 'Serine',
                    'UAU': 'Tyrosine',
                    'UAC': 'Tyrosine',
                    'UGU': 'Cysteine',
                    'UGC': 'Cysteine',
                    'UGG': 'Tryptophan',
                    'UAA': 'STOP',
                    'UAG': 'STOP',
                    'UGA': 'STOP',
                    }
    if len(strand) == 3:
        outputs.append(protein_dict.get(strand))

    elif len(strand) > 3:
        index = range(0, len(strand), 3)

        for i in index:
            start = i
            end = i + 3
            outputs.append(protein_dict.get(strand[start:end]))
    else:
        return []

    if "STOP" in outputs:
        ndx = outputs.index('STOP')
        return outputs[:ndx]

    return outputs

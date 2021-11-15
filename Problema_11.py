import itertools

multime = {'A', 'B', 'C', 'D'}

for lengh in range(len(multime)):
    subm = itertools.combinations(multime, lengh + 1)

    print(f'Submultimile multimii {multime}, de lungimea {lengh + 1} sunt:\n{set(subm)}')
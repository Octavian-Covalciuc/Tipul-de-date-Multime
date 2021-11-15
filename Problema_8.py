try:
    num1 = set(map(int, input('Dati numare(separate prin spatiu): ').split()))
    num2 = set(map(int, input('Dati numare(separate prin spatiu): ').split()))
    print(f'Intersectia multimilor este {num1.intersection(num2)}')
    print(f'Reuniunea multimilor este {num1.union(num2)}')
    print(f'Diferenta multimilor este A-B{num1.difference(num2)}; B-A{num2.difference(num1)}')
except:
    print('Introduceti numere in liste')
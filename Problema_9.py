import string

lit1 = set(input('Dati litere mari(separate prin spatiu): ').split())
lit2 = set(input('Dati litere mari(separate prin spatiu): ').split())
if lit1.issubset(list(string.ascii_uppercase)) & lit2.issubset(list(string.ascii_uppercase)):
    print(f'Intersectia multimilor este {lit1.intersection(lit2)}')
    print(f'Reuniunea multimilor este {lit1.union(lit2)}')
    print(f'Diferenta multimilor este A-B{lit1.difference(lit2)}; B-A{lit2.difference(lit1)}')
else:
    print('Formati multimi din litere mari ale alfabetului latin')
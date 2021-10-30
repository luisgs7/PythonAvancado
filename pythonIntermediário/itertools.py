from itertools import combinations, permutations, product

nomes = ['nome1', 'nome2', 'nome3', 'nome4']

print("Combinations")
for grupo in combinations(nomes, 2):
    print(grupo)

print("\nPermutations")
for grupo in permutations(nomes, 2):
    print(grupo)

print("\nProduct")
for grupo in product(nomes, repeat=2):
    print(grupo)
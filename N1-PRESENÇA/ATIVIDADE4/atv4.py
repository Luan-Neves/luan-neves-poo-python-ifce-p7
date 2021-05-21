l = []

for f in range(3):
    l.append(int(input(f'Digite o comprimento {f+1}: ')))

if l[0] == l[1] and l[1] != l[2] or l[0] == l[2] and l[2] != l[1] or l[2] == l[1] and l[1] != l[0]:
    print(f"\nO Triângulo é isósceles!\n")
elif l[0] == l[1] and l[0] == l[2]:
    print(f"\nO Triângulo é equilátero!\n")
else:
    print(f"\nO Triângulo é escaleno!\n")
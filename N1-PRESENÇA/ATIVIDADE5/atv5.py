def c(entrada):
    ver1 = entrada[0] + entrada[1]
    ver2 = entrada[0] + entrada[2]
    ver3 = entrada[1] + entrada[2]

    if entrada[0] <= 0 or entrada[1] <= 0 or entrada[2] <= 0:
        print("\nFalse")
    elif entrada[2] >= ver1 or entrada[1] >= ver2 or entrada[0] >= ver3:
        print('não forma triangulos')
    else:
        print('forma triangulos')

cc = []

for x in range(3):
    cc.append(int(input(f'Digite o tamanho do canudo {x+1}: ')))

c(cc)
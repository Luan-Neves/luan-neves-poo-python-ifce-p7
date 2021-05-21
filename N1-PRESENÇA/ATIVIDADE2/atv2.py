lista = []
def pi(list,alt):
    if alt == '1':
        list.insert(0,input('digite o valor: '))
    elif alt == '0':
        list.pop(0)
    else: 
        print('Opção inválida.')
    
    return list
def fi(list,alt):
    if alt == '1':
        list.append(input('digite o valor: '))
    elif alt == '0':
        list.pop(0)
    else: 
        print('OPÇÃO NÃO É VÁLIDA')

    return list
def li(list,alt):
    if alt == '1':
        list.insert(int(input('elemento: ')),input('digite o valor: '))
    elif alt == '0':
        list.pop(int(input('elemento: ')))
    else: 
        print('OPÇÃO NÃO É VÁLIDA')
    return list

while 1:
    n = input('1: pilha\n2: fila\n3: lista encadeada\n4: Mostrar lista\noutra, sair.\nDigite uma opção: ')
    if n == '1':
        lista = pi(lista,input('\nremover 0\ninserir 1\n\nDigite uma opção: '))
    elif n == '2':
        lista = fi(lista,input('\nremover 0\ninserir 1\n\nDigite uma opção: '))
    elif n == '3':
        lista = li(lista,input('\nremover 0\ninserir 1\n\nDigite uma opção: '))
    elif n == '4':
        print(f'Lista: {lista}')
    else:
        break

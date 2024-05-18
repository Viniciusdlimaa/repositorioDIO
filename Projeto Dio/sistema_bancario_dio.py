saldo = 0
limite_dia = 0
tipo_extrato = dict()
extrato = list()


while True: 
    print('--'*30)
    print('[1]Deposito\n[2]Saque\n[3]Extrato')
    operacao = int(input('Qual sera sua operação? '))
    if operacao == 1:
        valor_deposito = int(input('Valor do deposito: '))
        saldo = saldo + valor_deposito
        print(f'Saldo: {saldo}')
    elif operacao == 2:
        saque = int(input('Informe o valor do saque: '))
        if limite_dia == 3:
            print('Voce ja atingiu o limite de saque diario, tente novamente amanha')
        elif saque > saldo:
            print('Falha, valor maior do que seu saldo')
            print(f'Saldo atual: {saldo}')
        elif saque > 500:
            print('Ops, voce só pode fazer saques ate R$500')
        else:
            saldo = saldo - saque
            print(f'Saque feito com sucesso!\nSaldo atual: {saldo}')
            limite_dia = limite_dia + 1
            tipo_extrato['Saque'] = saque
            extrato.append(tipo_extrato.copy())
            tipo_extrato.clear()
    elif operacao == 3:
        for i, v in enumerate(extrato):
            print(v)
    print('--'*30)
    while True:
        resp = int(input('[1]Sim\n[2]Não\nDeseja continuar? '))
        if resp == 1 or resp == 2:
            break
        else:
            print('ERRO! Digite um valor 1 ou 2')
    if resp == 2:
        break

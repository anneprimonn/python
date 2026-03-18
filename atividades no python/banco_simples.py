senha = int(input('Informe a senha: '))
saldo = 0
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

if senha == 123:
    print('\n1-Extrato')
    print('2-Deposito') 
    print('3-Saque') 
    print('4-Sair') 
    resp = int(input('Digite o que deseja: '))
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

    if resp == 1:
        print('\n2Seu extratro é de:',saldo)

    elif resp == 2:
        depo = float(input('\nDigite o quanto quer depositar: '))
        print('Seu deposito é de: +',depo)
        saldo = depo + saldo
        print('seu saldo é de: ',saldo)

    elif resp == 3:
        saque = float(input('\nDigite o quanto quer sacar: '))
        print('Seu deposito é de: -',saque)
        saldo = saque - saldo
        print('seu saldo é de: ',saldo)

    elif resp == 4:
        print('Encerrado.')
        print('seu saldo é de: ',saldo)

    else:
        print('Opção Inválida')
else:
    print('Senha Inválida')

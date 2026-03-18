while True:
    try:
        print('\n1-Soma')
        print('2-Subitraçao') 
        print('3-Multiplicação') 
        print('4-Divisao') 
        escolha = int(input('Qual operação deseja: '))


        if escolha == 1:
            a = int(input('\nDigite o numero: '))
            b = int(input('Digite o numero: '))
            for n in range(1):
                print(f'\n{a} + {b} = {a+b}')
            
        elif escolha == 2:
            a = int(input('\nDigite o numero: '))
            b = int(input('Digite o numero: '))
            for n in range(1):
                print(f'\n{a} - {b} = {a-b}')
        
        elif escolha == 3:
            a = int(input('\nDigite o numero: '))
            b = int(input('Digite o numero: '))
            for n in range(1):
                print(f'\n{a} X {b} = {a*b}')

        elif escolha == 4:
            a = int(input('\nDigite o numero: '))
            b = int(input('Digite o numero: '))
            for n in range(1):
                print(f'\n{a} / {b} = {a/b}')

        else:
            print('\nescolha invalida')
    except:
        print('\nerro ')

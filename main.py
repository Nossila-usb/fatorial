# FUNCAO fatorial
def fatorial(n):
   if n == 0:
    return 1
   else:
    return n * fatorial(n - 1)

# programa principal
if __name__=='__main__':
    try:
        n = int(input('Informe um numero inteiro positivo: '))

        if n >= 0:
           print(f'O fatorial de {n} e {fatorial(n)}.')
        else:
           print(f'Não existe fatorial de {n}.')
    except:
       print('Não foi possivel calcular o fatorial.')


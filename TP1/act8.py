print('vamos a sacar tu indice de masa corporal')
altura = float(input('decime tu altura '))
peso = float(input('decime tu peso '))

imc = float(peso/(altura**2))

print(f'Tu IMC es {imc}')
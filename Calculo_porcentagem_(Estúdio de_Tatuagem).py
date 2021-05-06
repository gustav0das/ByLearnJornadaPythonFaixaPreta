tatuador = input('Digite o nome do tatuador: ')

Valor = float(input('Digite o valor da Tattoo: '))
forma_pagamento = input('Digite a forma de pagamento: ')

#Forma de pagamento

if forma_pagamento == 'Débito':
  Valor = Valor * 0.9801
elif forma_pagamento == 'Crédito':
  Valor = Valor * 0.9575
else:
  Valor = Valor

# Cálculo de porcentagem

if tatuador == 'Ana' or tatuador == "Marina": 
  valor_porcentagem = Valor * 0.05
  print(f'{tatuador} precisa pagar {valor_porcentagem:.2f} para o estúdio')
else:
  valor_porcentagem = Valor *  0.3
  print(f'{tatuador} precisa pagar {valor_porcentagem:.2f} para o estúdio')


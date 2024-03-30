# Estruturas condicionais
# Condicional Simples (If)
# Condicional Composta (If-Else)

# digito = int(input('Digite um número'))
# if(digito > 10):
#     print(f'O valor {digito} é maior que 10')
# else:
#     print(f'O valor {digito} é menor que 10')



# digito = int(input('Digite sua idade'))
# if(digito > 18):
#     print(f'O valor {digito} é maior que 18. Pode Dirigir.')
# else:
#     print(f'O valor {digito} é menor que 18. Não pode dirigir')


# Operadores Lógicos (Ou Boleanos)
# not
# and
# or


# nota1 = float(input("Digite a nota da matéria 1: "))
# nota2 = float(input("Digite a nota da matéria 2: "))
# nota3 = float(input("Digite a nota da matéria 3: "))
# if (nota1 >= 7 and nota2 >= 7 and nota3 >= 7):
#     print('Aprovado')
# else:
#     print('Reprovado')


# digito = int(input('Digite um número'))
# if(digito > 10):
#     print(f'O valor {digito} é maior que 10')
# else:
#     if(digito < 10):
#         print(f'O valor {digito} é menor que 10')
#     else:
#         print(f'O valor {digito} é igual que 10')


# print('Opções de frutas: ')
# print('1 - maça ')
# print('2 - laranja ')
# print('3 - banana ')
# escolha = int(input('Digite sua escolha: '))
# quantidade = int (input('Quantas unidades deseja comprar? '))
# if(escolha == 1):
#     pagar = 2.3 * quantidade
#     print(f'Você comprou {quantidade} maças. Total a pagar {pagar}')
# else:
#     if(escolha == 2):
#         pagar = 3.6 * quantidade
#         print(f'Você comprou {quantidade} laranjas. Total a pagar {pagar}')
#     else:
#         pagar = 1.85 * quantidade 
#         print(f'Você comprou {quantidade} bananas. Total a pagar {pagar}')

# print('Opções de frutas: ')
# print('1 - maça ')
# print('2 - laranja ')
# print('3 - banana ')
# escolha = int(input('Digite sua escolha: '))
# quantidade = int (input('Quantas unidades deseja comprar? '))
# if(escolha == 1):
#     pagar = 2.3 * quantidade
#     print(f'Você comprou {quantidade} maças. Total a pagar {pagar}')
# elif(escolha == 2):
#     pagar = 3.6 * quantidade
#     print(f'Você comprou {quantidade} laranjas. Total a pagar {pagar}')
# elif (escolha == 3):
#     pagar = 1.85 * quantidade 
#     print(f'Você comprou {quantidade} bananas. Total a pagar {pagar}')
# else:
#     print('Escolha inválida')


print('Pagamento: ')
print('1 - à vista')
print('2 - parcelamento em 3x')
print('3 - parcelamento em 5x')
print('4 - parcelamento em 10x')
print('Precione outra telcla para sair.')
opcao = int(input('Digite sua opção de pagamento: '))
valor = float(input('Digite o valor do produto: '))

if(opcao == 1):
    valor_final = valor*0.95
    print('Produto comprado à vista. Total a pagar: R$ {valor_final}')
elif(opcao == 2):
    valor_final = valor
    parcela = valor_final / 3
    print('Produto comprado em 3x. Total a pagar: R$ {valor_final} em 3 parcelas de R$ {parcela:.2f}.')
elif(opcao == 3):
    valor_final = valor*1.02
    parcela = valor_final / 5
    print('Produto comprado em 5x. Total a pagar: R$ {valor_final} em 5 parcelas de R$ {parcela:.2f}.')
elif(opcao == 4):
    valor_final = valor*1.08
    parcela = valor_final / 10
    print('Produto comprado em 10x. Total a pagar: R$ {valor_final} em 10x parcelas de R$ {parcela:.2f}.')
else:
    print('Opção inválida. Xau!')
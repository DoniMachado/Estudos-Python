# i = 10
# while(i >= 0):
#     print(i)
#     i = i - 1
# print("Fogo!")



# inicial = int(input('Digite um número inicial para a contagem'))
# final = int(input('Digite outro número inteiro para ser o número final da contagem'))
# while(inicial < final):
#     if(inicial % 2 == 0):
#         print(inicial)
#     inicial = inicial + 1

# inicial = int(input('Digite um número inicial para a tabuada'))
# i = 0
# while(i <= 10):
#     resultado = i * inicial
#     print(f"Tabuada: {inicial} * {i} = {resultado}")
#     i = i+1

# i = 1
# soma = 0
# while (i <= 5):
#     num = int(input(f'Digite o {i} º número: '))
#     soma = num + soma
#     i = i+1
# print(f"Somátorio: {soma}")
# print(f"Média: {soma/5}")


# x = int(input('Digite um número: '))
# y = int(input('Digite outro número: '))
# i = 1
# soma = 0
# while(i <= y):
#     soma = soma + x
#     i = i+1
# print(f"Valores digitados: x = {x} e y = {y} e o resultado da multiplicação será: {soma}")


# inicial = int(input('Digite um número inicial para a contagem'))
# final = int(input('Digite outro número inteiro para ser o número final da contagem'))
# i = inicial
# qtd_positivos = 0
# qtd_par = 0
# qtd_impar = 0
# soma_positivos = 0
# soma_par = 0
# soma_impar = 0
# if (inicial < final):
#     while(i <= final):
#         if(i > 0):
#             qtd_positivos = qtd_positivos + 1
#             soma_positivos = soma_positivos + i
#         if(i % 2 == 0):
#             qtd_par = qtd_par + 1
#             soma_par = soma_par + i
#         else:
#             qtd_impar = qtd_impar + 1
#             soma_impar = soma_impar + i
#         i = i + 1 
#     media_positivo = soma_positivos/qtd_positivos
#     media_par = soma_par/ qtd_par
#     media_impar = soma_impar/qtd_impar
#     print(f"Quantidade de valores positivos: {qtd_positivos}") 
#     print(f"Somatória dos valores positivos: {soma_positivos}")
#     print(f"Média dos valores positivos: {media_positivo}") 
#     print(f"Quantidade de valores pares: {qtd_par}") 
#     print(f"Somatória dos valores pares: {soma_par}")
#     print(f"Média dos valores pares: {media_par}") 
#     print(f"Quantidade de valores impares: {qtd_impar}") 
#     print(f"Somatória dos valores impares: {soma_impar}")
#     print(f"Média dos valores impares: {media_impar}") 
# else:
#     print(f"Você digitou os valores: inicial = {inicial} e final = {final}. Sendo o número inicial maior que o número final")




# while(True):
#     idade = int(input("Digite sua idade: "))
    
#     if(idade < 0):
#         break

#     sexo = input("Digite seu gênero M ou F: ")

#     if(sexo == 'M' or sexo == 'm'):
#         print(f'Boa noite senhor. Sua idade é {idade}')
#     elif(sexo == 'F' or sexo == 'f'):
#         print(f'Boa noite senhora. Sua idade é {idade}')
#     else:
#         print('Sexo inválido')
# print("Encerrando...")



# while(True):
#     texto = input("Digite uma frase: ")
#     tamanho = len(texto)
#     print(texto)
#     print(texto.replace(" ",""))
#     if(tamanho < 10 or tamanho > 30):
#         break
# print("Encerrando...")



# qtd = 0
# soma = 0
# while True:
#     num = int(input("Digite um número inteiro: "))
#     if(num < 0):
#         break
#     qtd += 1
#     soma += num

# media = soma/qtd
# print(f'A média dos valores digitados é {media}')

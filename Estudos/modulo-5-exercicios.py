# linguagens = ('JavaScript','Rust','Swift','Python','Kotlin','Go','C#','Dart','Julia','TypeScript')

# i = 0
# while(linguagens[i] != 'Python'):
#     i+=1
# print(f'Encontramos o {linguagens[i]} no index {i} ou {i+1}º posição')



# def func(mensagem, *num):
#     maior = num[0]
#     for i in num:
#         if maior < i:
#             maior = i
#     print(mensagem,maior)


# func('Maior',1,2,3)

# x = [1,2,40,5,100,-1]

# maior = x[0]
# for i in x:
#     if i > maior:
#         maior = i

# print(maior)

# def maiorIMC(lista):
#     maior = lista[0][3]
#     for i in lista:
#         if i[3] > maior:
#             maior = i[3]
#     return maior

# def menorIMC(lista):
#     menor = lista[0][3]
#     for i in lista:
#         if i[3] < menor:
#             menor = i[3]
#     return menor

# lista = []
# imc = lambda p,h :  p /(h ** 2)
# while True:     
#     nome = input("Digite o seu nome: ")
#     altura = float(input("Digite sua altura: "))
#     peso = float(input("Digite seu peso: "))  
#     lista.append([nome,altura,peso, imc(peso,altura)])  
#     continuar = input("Deseja continuar? Digite N para sair: ")
#     if(continuar.lower() == 'n'):
#         break  

# print(f'Cadastros: {lista}') 
# print(f'Quantidade de pessoas: {len(lista)}')
# print(f'Maior IMC: {maiorIMC(lista)}')
# print(f'Menor IMC: {menorIMC(lista)}')
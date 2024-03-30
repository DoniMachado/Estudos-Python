#TUPLAS (TUPLE)

#mochila = ("Laptop","Carteira","Carregador de Celular","Celular","Chaves")
# print(mochila)
# print(mochila[0])
# print(mochila[1])
# print(mochila[-1])
# print(mochila[0:])
# print(mochila[:3])

# isso não pode gera erro
# mochila[1] = "Tablet"

# for item in mochila:
#     print(item)

# upgrade = ("Tablet","Lanche")
# nova_mochila = mochila + upgrade
# for item in nova_mochila:
#     print(item)


# def soma(*num):
#     soma = 0
#     print(f'Tupla: {num}')
#     for i in num:
#         soma += i
#     return soma

# print(soma(1,2))
# print(soma(1,2,3,4,5))



#LISTAS (LIST)
# mochila = ["Laptop","Carteira","Carregador de Celular","Celular","Chaves"]
# print(mochila)
# print(mochila[0])
# print(mochila[1])
# print(mochila[-1])
# mochila.append('Oculos')
# mochila.insert(1,'Boné')
# print(mochila)
# print(mochila[0])
# print(mochila[1])
# print(mochila[-1])
# mochila.remove('Oculos')
# del mochila[1]
# print(mochila)
# print(mochila[0])
# print(mochila[1])
# print(mochila[-1])

# Cópia errada, isso só copia o endereço de memória
# x = [1,2,3,4,5]
# y = x
# y[0] = 12
# print(x)
# print(y)



# Cópia correta, isso cópia os valores para um outro endereço de memória
# x = [1,2,3,4,5]
# y = x[:]
# y[0] = 12
# print(x)
# print(y)

# Cópia correta tbm
# x = [1,2,3,4,5]
# y = x.copy()
# y[0] = 12
# print(x)
# print(y)


#DICIONÁRIO (DICT)

# dict = {'Laptop':13, 'Tablet': 3 , 'Smartphone':5}

# print(dict)
# print(dict['Laptop'])
# print(dict.values())
# print(dict.keys())

# for chave,dado in dict.items():
#     print(chave,dado)






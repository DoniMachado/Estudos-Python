# def cage(str):
#     tam = len(str)
#     if(tam):
#         print('+','-'*tam,'+')
#         print('|',str,'|')
#         print('+','-'*tam,'+')

# cage("teste")
# cage("Curso de Python")
# cage('')


# def contagem(final,init=1,incre=1):
#     for i in range(init,final+1,incre):
#         print(i, end=' ')
#     print('\n')

# contagem(10)

# def ordenar(x=0,y=0,z=0):
#     list = [x,y,z]
#     list.sort(True,)
#     for i in list:
#         print(i)

# x = int(input("Digite um primeiro número: "))
# y = int(input("Digite um segundo número: "))
# z = int(input("Digite um terceiro número: "))
# ordenar(x,y,z)


# def valida_string(frase,min,max):
#     str = input(frase)
#     tam = len(str)
#     while(tam < min or tam > max):
#         str = input(frase)
#         tam = len(str)
#     return str

# min = 1
# max = 10
# res = valida_string(f"Digite uma string de tamanho entre {min} e {max} caracteres: ",min,max)
# print(f'Você digitou a string: {res}. Que é uma string válida com quantidade de caracteres entre {min} e {max}')


# def valida_int(frase):
#     i = int(input(frase))    
#     while(i < 0):
#         i = int(input(frase))  
#     return i

# def fatorial(num):
#     fat = 1   
#     while(num >= 1):
#         fat *= num
#         num -= 1
#     return fat

# num = valida_int("Digite um número inteiro positivo para saber seu fatorial: ")
# res = fatorial(num)
# print(f'O fatorial de {num} é {res}')



# calc = lambda a,b: (a+5)*b
# print(calc(5,10))
    
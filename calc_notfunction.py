# -*- encoding: utf-8 -*-

print ("Escolha a operação desejada:\n")

print ("Soma:           1")
print ("Subtração:      2")
print ("Multiplicação:  3")
print ("Divisão:        4 \n")
x = int(input ("Digite  1, 2, 3, ou 4 e tecle enter: \n"))

a = float(input("Digite o número 1 e tecle enter: \n"))
b = float(input("Digite o número 2 e tecle enter: \n"))

if  x == 1 :
    res = a + b
    print(a, "+", b, "=", res,"\n")
elif x == 2:
    res = a - b
    print(a, "-", b, "=", res, "\n")
elif x == 3:
    res = a * b
    print(a, "*", b, "=", res,"\n")
elif x == 4:
    res = a / b
    print(a, "/", b, "=", res,"\n")
else:
    res = "Operação Inválida"
    print (res)
print ("O resultado é:", res,"\n")

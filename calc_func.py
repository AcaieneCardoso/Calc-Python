''' Very Simple Python Calc '''
''' Author: Acaiene Cardoso'''
                
# Função soma dois números
def soma(x, y):
   return x + y

# Função subtrai dois números
def subtrai(x, y):
   return x - y

# Função multiplica dois números
def multiplica(x, y):
   return x * y

# Função divide dois números
def divide(x, y):
   return x / y

print("\n\nSelecione a operação desejada:")
print("1.Soma")
print("2.Subtrai")
print("3.Multiplica")
print("4.Divide")

# Verifica opção do usuário
opcao = input("\nEntre com a opção (1,2,3,4):\n")

num_1 = float(input("Entre com primeiro número e tecle enter: \n"))
num_2 = float(input("Entre com segundo número e tecle enter: \n"))

if opcao == '1':
   print(num_1,"+",num_2,"=", soma(num_1,num_2))

elif opcao == '2':
   print(num_1,"-",num_2,"=", subtrai(num_1,num_2))

elif opcao == '3':
   print(num_1,"*",num_2,"=", multiplica(num_1,num_2))

elif opcao == '4':
   print(num_1,"/",num_2,"=", divide(num_1,num_2))
else:
   print("Entrada Inválida")

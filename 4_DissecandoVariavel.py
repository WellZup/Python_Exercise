a = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ",a.isalpha())
print("Está em maiúsculas? ",a.isupper())
print("Está em minusculos",a.islower())
print("Está com a primeira maiúscula?",a.istitle())
# Programa pede a String e Armazena ela na variavel
string = input("Digite a string a ser invertida: ")

# Variavel que armazenará a String original
stringinv = ""

# Processo para inverter a String
for i in range(len(string)-1, -1, -1):
    stringinv += string[i]

# Print das Strings
print("String original: ", string)
print("String invertida: ", stringinv)
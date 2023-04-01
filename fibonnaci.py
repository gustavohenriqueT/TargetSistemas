def fib(n):

# Função que retorna o valor da sequência de Fibonacci para o índice n.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Pede para o usuário informar um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
pertencefib = False
for i in range(numero):
    if fib(i) == numero:
        pertencefib = True
        break

# Imprime o resultado
if pertencefib:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

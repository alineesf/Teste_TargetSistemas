#QUESTÃO 1
indice  = 13
soma = 0 
K = 0

while K < indice:
    K += 1 
    soma += K 

print("O valor da soma é:", soma)







#QUESTÃO 2
def fibonacci_sequence(n):
    if not isinstance(n, int) or n < 0:
        return "Erro: O argumento deve ser um número inteiro positivo."
    
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_fibonacci_number(num):
    if not isinstance(num, int) or num < 0:
        return "Erro: O número não deve ser negativo."
    
    fib_sequence = fibonacci_sequence(num)
    if isinstance(fib_sequence, str):
        return fib_sequence
    
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

try:
    numero = int(input("Informe um número: "))
    print(is_fibonacci_number(numero))
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")






#QUESTÃO 4
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
faturamento_total = sum(faturamento.values())


if faturamento_total == 0:
    print("Erro: Não é possível calcular.")
else:
    for estado, valor in faturamento.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")






#QUESTÃO 5
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string_original = input("Digite uma string: ")

if string_original == "":
    print("Erro: A string não pode estar vazia.")
else:
    string_invertida = inverter_string(string_original)
    print(f"String invertida: {string_invertida}")


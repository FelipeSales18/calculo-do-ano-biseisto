# exercico 1

a =int(input("valor do a: "))
b =int(input("valor do b : "))
c =int(input("valor do c: "))

delta= b * b -(4) * a * c

raiz1 =(-b+delta ** 0.5) / 2 * a
raiz2 =(-b-delta ** 0.5) / 2 * a
print("o resultado da raiz 1 é: ",raiz1)
print("o resultado da raiz 2 é: ",raiz2)

# exercicio 2

print("hello world")

ano = int(input("Qual ano você está: "))

print(ano % 4==0 and ano % 100!=0)
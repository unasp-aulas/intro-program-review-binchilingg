n = 1
soma = 0
while True:
  x = int(input(f"digite o {n} numero: "))
  if x == 0:
    break
  soma += x
  n += 1
print(soma)

import math

dados = [70, 99, 36, 27, 81, 61, 72, 26, 56, 98, 26, 33, 92, 73, 45, 42, 97, 48, 99, 93, 49, 80, 22, 58, 75, 49, 74, 67, 72, 71, 73, 82, 52, 62, 72]
dados.sort()


total = 35
k = 1 + (3.3*(math.log10(total)))
valor_max = max(dados)
valor_min = min(dados)
a_total = valor_max - valor_min
a_intervalo = a_total / k

print(f'A massa total de dados é {len(dados)}')
print("A quantidade de classes é {}".format(round(k)))
print("Amplituda máxima é {}".format(a_total))
print("Amplitude por intervalo é {}".format(round(a_intervalo)))

print("")
print("="*10, "classe", "="*10)
print("")

soma = 0
conversor = round(k)
for i in range(conversor):
    print("[",round(valor_min + soma), "|-", round(valor_min+a_intervalo+soma),"]")
    soma = soma + a_intervalo
